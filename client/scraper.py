import requests

class Scraper:
    authorization = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    guest_token = False
    guest_url = 'https://api.twitter.com/1.1/guest/activate.json'
    user_by_screenname = lambda self, screen_name: 'https://twitter.com/i/api/graphql/ZRnOhhXPwue_JGILb9TNug/UserByScreenName?variables=%7B%22screen_name%22%3A%22' + screen_name + '%22%2C%22withHighlightedLabel%22%3Atrue%7D'
    user_timeline = lambda self, user_id: 'https://api.twitter.com/2/timeline/profile/' + user_id + ".json" +\
            "?include_profile_interstitial_type=0"+\
            "&tweet_mode=extended"+\
            "&include_tweet_replies=false"+\
            "&userId=" + user_id+\
            "&count=20" +\
            "&ext=mediaStats%2ChighlightedLabel"
    local_api = 'http://127.0.0.1:8080/tweets'
    local_api_active = False
    screen_name = False
    user_id = False
    tweets = {}

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.get_guest_token()
        self.get_user_id()
        self.local_api_active = self.check_local_api()

    def get_guest_token(self):
        headers = {
            "Authorization": self.authorization
            }

        try:
            response = requests.post(self.guest_url, headers=headers).json()
        except Exception as e:
            print("Error getting guest token \n" + str(e))
            return

        self.guest_token = response["guest_token"]

    def get_user_id(self):
        headers = {
            "Authorization": self.authorization, 
            "x-guest-token": self.guest_token,
            }

        try:
            response = requests.get(self.user_by_screenname(self.screen_name), headers=headers).json()
        except Exception as e:
            print("Error getting user ID \n" + str(e))
            return

        try:
            self.user_id = response["data"]["user"]["rest_id"]
        except Exception as e:
            print("Error getting user ID: User may not exist \n" + str(e))
            return
    
    def get_tweets(self, limit):
        headers = {
            "Authorization": self.authorization, 
            "x-guest-token": self.guest_token
            }

        try:
            response = requests.get(self.user_timeline(self.user_id), headers=headers).json()
        except Exception as e:
            print("Error getting user tweets\n" + str(e))
            return

        try:
            user_timeline = response["timeline"]["instructions"][0]["addEntries"]["entries"]
            user_tweets = response["globalObjects"]["tweets"]
        except Exception as e:
            print("No tweets found, is the profile private or inactive?\n" + str(e))
            return

        new_tweets = {t["sortIndex"]:user_tweets[t["sortIndex"]]["full_text"] for t in user_timeline if "item" in t["content"] and t["sortIndex"] not in self.tweets}
        limit = min(limit, len(new_tweets))
        self.process_tweets(new_tweets)
        self.display_tweets(new_tweets, limit)
    
    def process_tweets(self, new_tweets):
        for t in reversed(list(new_tweets.items())):
            self.tweets[t[0]] = t[1]
        
    def display_tweets(self, new_tweets, limit):
        for t in reversed(list(new_tweets.items())[:limit]):
            print(t[1] + '\n')
            if(self.local_api_active): self.save_tweet(t[1])
    
    def check_local_api(self):
        try:
            requests.get(self.local_api)
            return True
        except:
            return False
    
    def save_tweet(self, tweet):
        try:
            requests.post(self.local_api, json=tweet)
        except Exception as e:
            print("API Error " + str(e))
            return
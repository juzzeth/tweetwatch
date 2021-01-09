import requests
import constants
import sys

class Scraper: 
    guest_token = None
    local_api_active = False
    screen_name = None
    user_id = None
    error = None
    tweets = {}

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.get_guest_token()
        if(self.guest_token): self.get_user_id()
        if(self.user_id): self.local_api_active = self.check_local_api()

    def get_guest_token(self):
        headers = {
            "Authorization": constants.AUTHORIZATION
            }

        try:
            response = requests.post(constants.GUEST_URL, headers=headers).json()
        except:
            self.error = "Error getting guest token from Twitter"
            return

        self.guest_token = response["guest_token"]

    def get_user_id(self):
        headers = {
            "Authorization": constants.AUTHORIZATION, 
            "x-guest-token": self.guest_token,
            }

        try:
            response = requests.get(constants.USER_BY_SCREENNAME(self.screen_name), headers=headers).json()
        except:
            self.error = "Error getting user ID: Twitter gave no response."
            return

        try:
            self.user_id = response["data"]["user"]["rest_id"]
        except:
            self.error = "Error getting user ID: User may not exist."
            return
    
    def get_tweets(self, limit):
        headers = {
            "Authorization": constants.AUTHORIZATION, 
            "x-guest-token": self.guest_token
            }

        try:
            response = requests.get(constants.USER_TIMELINE(self.user_id), headers=headers).json()
        except:
            self.error = "Error getting user tweets."
            return

        try:
            user_timeline = response["timeline"]["instructions"][0]["addEntries"]["entries"]
            user_tweets = response["globalObjects"]["tweets"]
        except:
            self.error = "No tweets found, is the profile private or inactive?"
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
            sys.stdout.write(str(t[1]).encode('ascii', 'ignore').decode('ascii').replace('\n', ' ') + '\n')
            if(self.local_api_active): self.save_tweet(t[1])
    
    def check_local_api(self):
        try:
            requests.get(constants.LOCAL_API)
            return True
        except:
            return False
    
    def save_tweet(self, tweet):
        try:
            requests.post(constants.LOCAL_API, json=tweet)
        except Exception as e:
            sys.stdout.write("Local API Error " + str(e))
            return
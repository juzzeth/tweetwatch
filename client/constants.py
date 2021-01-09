AUTHORIZATION = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
GUEST_URL = 'https://api.twitter.com/1.1/guest/activate.json'
USER_BY_SCREENNAME = lambda screen_name: 'https://twitter.com/i/api/graphql/ZRnOhhXPwue_JGILb9TNug/UserByScreenName?variables=%7B%22screen_name%22%3A%22' + screen_name + '%22%2C%22withHighlightedLabel%22%3Atrue%7D'
USER_TIMELINE = lambda user_id: 'https://api.twitter.com/2/timeline/profile/' + user_id + ".json" +\
            "?include_profile_interstitial_type=0"+\
            "&tweet_mode=extended"+\
            "&include_tweet_replies=false"+\
            "&userId=" + user_id+\
            "&count=20" +\
            "&ext=mediaStats%2ChighlightedLabel"
LOCAL_API = 'http://127.0.0.1:8080/tweets'
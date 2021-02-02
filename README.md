**Note:** The bearer token in client/constants.py is meant to be public. This is used by client side on Twitter and is not a security risk.

# tweetwatch
Monitor tweets of a specified Twitter account

* Provide Twitter handle as an argument while starting the program
* No authentication or API key required
* No reliance on third party Twitter libraries
* Initially outputs 5 most recent tweets to stdout
* Monitors and displays up to 20 new tweets every 10 minutes
* API to collect and list tweets
* Dockerfile included

### Information
* The program ignores pinned tweets if they are not within the user's 5 last tweets as the requirement was to initially show the 5 most recent tweets.
* Only 5 tweets will be displayed initially, but further checks will display up to 20. Assumed as we probably want the max amount of tweets possible if someone goes on a rant.
* Tweets are shown from oldest to newest. Assumed because as new tweets are collected, they will proceed with this order. It makes for easy reading.
* Tweets include retweets. Retweets can hold important information and the retweeting user can add their own comments and media.
* Only tweet content text is displayed, no date/time/handle etc. Assumed as the requirement stated output tweet text.
* Line breaks have been replaced with spaces, assumed as the output is much nicer in the docker log. Easy to change in client/scraper.py

## Usage
### API
`python3 api/main.py`
GET/POST to /tweets

### Client
`python3 client/main.py HANDLE`
Handle = Twitter username to monitor

## Using Docker
1. `git clone https://github.com/juzzeth/tweetwatch.git`
2. `docker build -t tweetwatch .`
3. `docker run -p 8080:8080 tweetwatch HANDLE`


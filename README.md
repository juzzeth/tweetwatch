# tweetwatch
Monitor tweets of a specified Twitter account

* Provide Twitter handle as an argument while starting the program
* No authentication or API key required
* Initially outputs 5 most recent tweets to stdout
* Monitors and displays up to 20 new tweets every 10 minutes
* No reliance on third party Twitter libraries
* API to list collected tweets
* Dockerfile included

## Other Information
* The program ignores pinned tweets
* Only 5 tweets will be displayed initially, but further checks will display up to 20
* Output tweets from oldest to newest
* Includes retweets
* Only tweet content full text is displayed, no date/time/handle etc.
* API will only accept requests from 127.0.0.1
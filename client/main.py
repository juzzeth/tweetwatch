import sys
import scraper
import time

if __name__ == '__main__':
    s = scraper.Scraper('troyhunt')
    if(s.user_id):
        s.get_tweets(5)
        while s.error is None:
                time.sleep(600)
                s.get_tweets(20)
    
    sys.stdout.write(str(s.error))
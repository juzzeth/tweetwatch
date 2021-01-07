import sys
import scraper
import time

if __name__ == '__main__':
    s = scraper.Scraper(sys.argv[1])
    s.get_tweets(5)

    while True:
            time.sleep(600)
            s.get_tweets(20)
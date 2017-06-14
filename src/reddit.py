import praw
import requests
import os
import imgur
from downloader.py import download_image
from config import reddit as cr # Not commited

reddit = praw.Reddit(client_id= cr['id'],
                     client_secret= cr['secret'],
                     redirect_uri= "https://localhost:8080",
                     user_agent= 'Downloads wallpapers from r/wallpapers')


def get_links_from_sub(subreddit):  
    links = []  
    wp_subreddit = reddit.subreddit(subreddit)
    for s in wp_subreddit.hot(limit=20):
        links.appends(s.url)
    return links


    

def crawl_reddit(*subreddits):
    for sub in subreddits:
        links = get_links_from_sub(sub)
        for url in links:
            #Nearly all of Reddit's picture submissions are hosted on their host or on imgur. So special use-cases were created for them
            if "i.redd.it" in url:
                download_image(url)
            elif "imgur" in url:
                imgur_links = imgur.get_links(url) # Many imgur submission are albums, so this is necessary
                for url in imgur_links:
                    download_image(url)
                
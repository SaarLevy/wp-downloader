import praw
import requests
import os
import imgur
import shutil
from config import reddit as cr # Not commited

reddit = praw.Reddit(client_id= cr['id'],
                     client_secret= cr['secret'],
                     redirect_uri= "https://localhost:8080",
                     user_agent= 'Downloads wallpapers from r/wallpapers')


def crawl_sub(subreddit):  
    links = [{}]  
    wp_subreddit = reddit.subreddit(subreddit)
    for s in wp_subreddit.hot(limit=20):
        temp = {"url": s.url, "id": s.id}
        links.append(url.s)
    return links


def download_image(item, path):
    if 'i.reddi.it' in item['url']:
        r = requests.get(item['url'], stream=True)
        with open(item['id'], 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r

    elif 'imgur' in item:
        imgur.get_links(item['url'])



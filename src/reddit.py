import praw
import requests
from config import reddit as cr

reddit = praw.Reddit(client_id= cr['id'],
                     client_secret= cr['secret'],
                     redirect_uri= "https//localhost:8080",
                     user_agent= 'Downloads wallpapers from r/wallpapers')

print(reddit.auth.url(['identity'], '...', 'permanent'))

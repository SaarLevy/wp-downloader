from config import imgur as ic
import requests
import json

headers = {'authorization': 'Client-ID '+ic['id']}

def get_links(url):
    links = []
    sections = url.split('/') 
    link_hash = sections[len(sections) - 1]
    endpoint = get_endpoint(url)

    
def get_endpoint(url):
    links = []
    sections = url.split('/') 
    link_hash = sections[len(sections) - 1]
    api_url = 'https://imgur.api/3/'

    image_response = requests.request('GET', api_url+'image/' + link_hash, headers=headers)
    if image_response.status_code = 200:
        return 'image'

    album_response = requests.request('GET', api_url+'album/' + link_hash, headers=headers)    
    if album_response.status_code = 200:
        return 'album'
    
    gallery_response =requests.request('GET', api_url+'gallery/' + link_hash, headers=headers)
        return 'gallery'
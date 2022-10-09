
from pprint import pprint
import requests


def get_all_urls():
    links = []
    next_page = 1
    while next_page:
        r = requests.get("https://genius.com/api/artists/2300/songs?page={}&sort=popularity".format(next_page))
        
        if r.status_code != 200:
            print("API Inaccessible.")
            return
        
        response = r.json().get("response", {})
        
        songs = response.get("songs")
        links.extend([song.get("url") for song in songs])
        
        next_page = response.get("next_page")

get_all_urls()
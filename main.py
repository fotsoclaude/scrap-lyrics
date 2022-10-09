from pprint import pprint

import requests
from bs4 import BeautifulSoup

def extract_lyrics(url):
    r = requests.get(url)
    
    if r.status_code != 200:
        print("Page inaccessible.")
        return []
    
    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-6")
    
    if not lyrics:
        return extract_lyrics(url)
    
    for sentence in lyrics.stripped_strings:
        print(sentence)

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
    print(links)

extract_lyrics(url="https://genius.com/Adele-i-drink-wine-debuted-live-lyrics")
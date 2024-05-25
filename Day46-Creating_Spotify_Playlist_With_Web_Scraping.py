import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import pprint
import datetime as dt

# Authentication part spotify

CLIENT_ID = "xyz"
CLIENT_SECRET = "abc"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="ABC"
    )
)

user_id = sp.current_user()["id"]

# Scraping 100 songs from Billboard

song_date = input("Which Year do you want to travel to? Submit in YYYY-MM-DD format :")

url = "https://www.billboard.com/charts/hot-100/" + song_date

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

songs = [soup.find(name="h3",
                   class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").get_text().replace(
    "\t", "").replace("\n", "")]
songs_list = soup.find_all(name="h3",
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

for song in songs_list:
    x = song.get_text().replace("\n", "")
    y = x.replace("\t", "")
    songs.append(y)

url_list = []
for x in range(0, len(songs)):
    try:
        temp_url = sp.search(f'track:{songs[x]} year:{song_date[:4]}', limit=1, type="track")['tracks']['items'][
            0]['external_urls']['spotify']
        url_list.append(temp_url)
    except:
        print("Song Not Found")

# Adding songs to a new playlist

playlist_name=f"BillBoard 100 Songs on {song_date}"
playlist_description=f"It features top 100 songs on the BillBoard on {song_date}"
playlist =sp.user_playlist_create(user=user_id,name=playlist_name,public=False,description=playlist_description)

sp.playlist_add_items(playlist_id=playlist['id'],items=url_list)

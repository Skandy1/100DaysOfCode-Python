from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keys as K

REQ_URL = "https://www.billboard.com/charts/hot-100/"
user_input = input("Which year you wanna travel to? Type in the date (YYYY-MM-DD)")
res = requests.get(url=f"{REQ_URL}{user_input}")
res.raise_for_status()
data = res.text
soup = BeautifulSoup(data, 'html.parser')
select_span = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_list = [song.text for song in select_span]  # list of songs

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=K.CLIENT_ID,
    client_secret=K.CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

# song uris

song_uris=[]
year=user_input.split("-")[0]
for song in song_list:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify!")

# create a playlist
playlist_id = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False,
                                   description="Billboard 100 on this date")['id']

# add songs
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
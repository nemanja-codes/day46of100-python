from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "aae5872ac91b48ff9e0f36fb33f628df"
SPOTIFY_CLIENT_SECRET = "b08fcd976afb4529b93108367e8f46d2"
SPOTIPY_REDIRECT_URI = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

top100 = [song.getText().strip() for song in soup.find_all(name="h3", class_="a-no-trucate")]
# print(top100)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="312lv6efym25vkxculcs5kieado4")
                     )


USER_ID = sp.current_user()["id"]




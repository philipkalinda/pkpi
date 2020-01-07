import pandas as pd
import numpy as np
import requests
import spotipy


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid ="" 
secret = ""
username = "philipkalinda"

client_credentials_manager = SpotifyClientCredentials(
	client_id=cid,
	client_secret=secret
) 

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private user-read-private user-read-recently-played user-read-currently-playing'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

print(sp.current_user_playlists())
print('*'*200)

print(sp.me())
print('*'*200)

print(sp.current_user_playing_track())
print('*'*200)




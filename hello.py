import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import ids

redirect_uri = 'http://localhost:3000'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_uri = 'spotify:playlist:37i9dQZF1DX0011TOiJEnw'

results = sp.playlist_tracks(playlist_uri)
tracks = results['items']

if not os.path.exists('playlist_audio'):
    os.makedirs('playlist_audio')

for track in tracks:
    track_name = track['track']['name']
    track_preview_url = track['track']['preview_url']

    if track_preview_url:
        # Download the audio file
        response = requests.get(track_preview_url)
        if response.status_code == 200:
            with open(f'playlist_audio/{track_name}.mp3', 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download {track_name}")
    else:
        print(f"No preview available for {track_name}")
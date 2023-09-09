from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

cid = 'c4ef5ca0a62a464bae63c4dc44cef3d3'
secret = '86b0c8f6cccf46ccb4eb9eac3e53f369'
redirect_uri = 'http://localhost:3000'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                               client_secret=secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-library-read user-modify-playback-state user-read-playback-state'))


# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(client_credentials_manager
# =
# client_credentials_manager)


# Replace 'YOUR_PLAYLIST_ID' with the actual ID of the playlist
playlist_id = '37i9dQZF1DX0011TOiJEnw'
results = sp.playlist_tracks(playlist_id)

# Extract the first track from the playlist
first_track = results['items'][0]['track']

if first_track['preview_url']:
    preview_url = first_track['preview_url']
    sp.start_playback(uris=[first_track['uri']])

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process():
    data = request.get_json()
    name = data['name']
    email = data['email']

    # get data from spotify
# @app.route("/getSpotify")
# def getSpotify():
#     GET/playlists{37i9dQZF1DX0011TOiJEnw}

    

    # Return response back to frontend if connection successful
    response = {
        "status": "success",
        "message": "Data received successfully!"
    }

    return jsonify(response)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  
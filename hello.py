from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'c4ef5ca0a62a464bae63c4dc44cef3d3'
secret = 'Your Secret ID'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process():
    data = request.get_json()
    name = data['name']
    email = data['email']

    # get data from spotify
@app.route("/getSpotify")
def getSpotify():
    

    # Return response back to frontend if connection successful
    response = {
        "status": "success",
        "message": "Data received successfully!"
    }

    return jsonify(response)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  
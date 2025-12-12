import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

songs = []
found_uris = []

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

def get_song_uri(song_name, artist_name=None):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET
    ))

    if artist_name:
        query = f"track:{song_name} artist:{artist_name}"
    else:
        query = f"track:{song_name}"

    try:
        result = sp.search(q=query, type='track', limit=1)

        tracks = result['tracks']['items']
        if tracks:
            uri = tracks[0]['uri']
            print(f"Found: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']}")
            return uri
        else:
            print(f"No match found for: {song_name}")
            return None
    except Exception as e:
        print(f"Error searching for {song_name}: {e}")
        return None


with open("song_list2.txt") as song_list:
    for song in song_list:
        songs.append(song)


for line in songs:
    if " - " in line:
        parts = line.split(" - ")
        song = parts[1]
        artist = parts[0]
        uri = get_song_uri(song, artist)
    else:
        uri = get_song_uri(line)

    if uri:
        found_uris.append(uri)

print(f"\nCollected {len(found_uris)} URIs ready for playlist creation.")
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

songs = []
found_uris = []

def get_song_uri(song_name, artist_name=None):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id = "ef56c951ec254ac0a7a71e3c21ba33f5",
        client_secret = "98818a78f96044b09b48e00392f28cbc"
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


with open("song_list.txt") as song_list:
    for song in song_list:
        songs.append(song)


for line in songs:
    if " - " in line:
        parts = line.split(" - ")
        song = parts[0]
        artist = parts[1]
        uri = get_song_uri(song, artist)
    else:
        uri = get_song_uri(line)

    if uri:
        found_uris.append(uri)

print(f"\nCollected {len(found_uris)} URIs ready for playlist creation.")
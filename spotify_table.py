import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_song_details(uri):
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
    if 'playlist' in uri:
        results = sp.playlist_tracks(uri)
        tracks = results['items']
    elif 'album' in uri:
        album = sp.album(uri)
        tracks = album['tracks']['items']
    else:
        print("Invalid link. Please provide a valid Spotify playlist or album link.")
        return ""

    table = "| Song | Artist | Album | Length |\n| --- | --- | --- | --- |\n"

    for track in tracks:
        song_name = track['track']['name'] if 'track' in track else track['name']
        artist_name = track['track']['artists'][0]['name'] if 'track' in track else track['artists'][0]['name']
        album_name = track['track']['album']['name'] if 'track' in track else album['name']
        duration_ms = track['track']['duration_ms'] if 'track' in track else track['duration_ms']
        duration_min_sec = divmod(duration_ms // 1000, 60)
        length = f"{duration_min_sec[0]:02}:{duration_min_sec[1]:02}"
        table += f"| {song_name} | {artist_name} | {album_name} | {length} |\n"

    return table

# Prompt user for album or playlist link
uri = input("Enter a Spotify playlist or album link: ")
output_table = get_song_details(uri)
print(output_table)

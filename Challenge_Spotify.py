"""
This program will be a Spotify assistant for the user
Users will be able to enter an artist and the program will show the Top10 songs of the artist
as well as its popularity on a scale from 0 to 100
    This program will create playlists for the user as well
"""

from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_ID, CLIENT_SECRET
import spotipy

def search_songs():
    artist = input("Type the name of an artist: ")
    results = sp.search(q=f'artist:{artist}', type='artist')

    if not results['artists']['items']:
        print(f"No information found for '{artist}'.")
        return None, None

    artist_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)

    # Storage popular songs
    popular_songs = top_tracks['tracks']
    show_popular_songs(popular_songs, artist)
    return popular_songs, artist

def show_popular_songs(songs, artist):
    print(f"\nTop 10 songs from {artist} are:\n")
    for i, song in enumerate(songs):
        print(f"{i + 1}. {song['name']} - Popularity: {song['popularity']}")

def create_playlist():
    playlist = []

    while True:
        try:
            selection = int(input("\nSelect a song (1-10) or type 0 to finish: "))
            if selection == 0:
                break
            elif 1 <= selection <= 10:
                selected_song = popular_songs[selection - 1]
                playlist.append(selected_song)
                print(f"\n== {selected_song['name']} added to playlist. ==")
                
                if len(playlist) >= 2:
                    total_time = sum([song['duration_ms'] for song in playlist])
                    total_time_minutes = total_time / 60000
                    print(f"Total Playlist duration: {total_time_minutes:.2f} minutes.")
                    
            else:
                print("Please enter a valid number (1-10).")
        except ValueError:
            print("Please enter a valid number (1-10).")
    return playlist

def show_playlist(playlist):
    if not playlist:
        print("\nNo songs on the playlist.\n")
    else:
        print("\n** Playlist has been completed... enjoy!:")
        print("Playlist:")
        for i, song in enumerate(playlist):
            duration_song_minutes = song['duration_ms'] / 60000
            print(f"{i + 1}. {song['name']} - Duration: {duration_song_minutes:.2f} minutes")
        print("")
        
# Use of credentials
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

# search of songs, artist and creation of playlist
popular_songs, artist = search_songs()

if popular_songs:
    playlist = create_playlist()
    show_playlist(playlist)
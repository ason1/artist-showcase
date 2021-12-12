import sys, spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# Initiliazes Spotipy client with valid scope, credentials
def init_client():

    if len(sys.argv) > 1: # Checks if user inputs valid username
        username = sys.argv[1]
    else:
        print('You need a username!') 
        sys.exit() # Exits script if username is not adequately provided

    scope = 'playlist-modify-public' # Write access to user's public playlists

    client_credentials = SpotifyClientCredentials() # API keys stored in environmental variables
    auth_manager = SpotifyOAuth(username=username, scope=scope) 
    sp = spotipy.Spotify(client_credentials_manager=client_credentials, auth_manager=auth_manager)
    print("Initializing client successful!")

    return sp

# Searches for associated URI for artist
def search_artist(sp, artist_name):

    query_artist_name = artist_name.replace(" ", "+") # Spotify query requires spaces encode with hex code %20 or +\
    result = sp.search(q=query_artist_name, limit=1, type='artist') 
    print("Searching for artist...")

    return result['artists']['items'][0]['uri'] # Spotify URI for search artist

# Searchess for the top tracks of specified artist
def search_tracks(sp, artist_uri):

    list = []
    result = sp.artist_top_tracks(artist_uri) # Spotify catalog information of the artist's top tracks
    
    print("Searching for top tracks...")
    for track in result['tracks']: # Iteration through results
        list.append(track['uri']) # Extract tracks' Spotify URI

    return list

# Creation of playlist 
def showcase_playlist(sp, artist_input):

    playlist_title = 'FEATURED ARTIST: ' + artist_input # Title of new playlist
    sp.user_playlist_create(user=sp.me()['id'], name=playlist_title) 

    user_playlists = sp.user_playlists(user=sp.me()['id']) # Extracts current user's playlist uris
    playlist_uri = user_playlists['items'][0]['uri'] # Extracts first playlist's uri (newly created playlist)

    return playlist_uri

# Adds extracted tracklist to newly created artist playlist
def playlist_pop(sp, tracklist, playlist_uri):

    sp.user_playlist_add_tracks(user=sp.me()['id'], playlist_id=playlist_uri, tracks=tracklist)
    print("Playlist created!")

if __name__ == '__main__':

    artist_input = input('Artist name: ')

    sp = init_client()
    artist_uri = search_artist(sp, artist_input)
    list = search_tracks(sp, artist_uri)
    playlist_uri = showcase_playlist(sp, artist_input)
    playlist_pop(sp, list, playlist_uri)
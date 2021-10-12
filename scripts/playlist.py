import sys, spotipy, json
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

    return sp

# Searches for associated URI for artist
def search_artist(sp, artist_name):

    query_artist_name = artist_name.replace(" ", "+") # Spotify query requires spaces encode with hex code %20 or +\
    result = sp.search(q=query_artist_name, limit=1, type='artist') 

    return result['artists']['items'][0]['uri'] # Spotify URI for search artist

if __name__ == '__main__':

    sp = init_client()
    URI = search_artist(sp, 'tyler the creator')
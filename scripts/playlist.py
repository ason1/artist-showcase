import sys, spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def init_client():

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print('You need a username!')
        sys.exit()

    SPOTIPY_REDIRECT_URI='localhost:8000'

    scope = 'playlist-modify-private'

    client_credentials = SpotifyClientCredentials()
    auth_manager = SpotifyOAuth(redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, username=username)
    sp = spotipy.Spotify(auth=auth_manager, client_credentials_manager=client_credentials)
    print('Successful authentication!')

    return sp

if __name__ == '__main__':

    sp = init_client()
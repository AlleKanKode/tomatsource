'''
Denne fil er oprindeligt skabt af Claude.ai ved at jeg har spurgt :
- Python code that can create a playlist in spotify
- Se Claudes beskrivende svar i spotiUp.md filen
'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys

def create_spotify_playlist(playlist_name, playlist_description, tracks):
    """
    Create a Spotify playlist and add tracks to it.
    
    Args:
        playlist_name (str): Name of the playlist to create
        playlist_description (str): Description of the playlist
        tracks (list): List of Spotify track URIs to add to the playlist
    
    Returns:
        dict: Playlist information if successful, None if failed
    """
    try:
        # Initialize Spotify client with necessary permissions
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='playlist-modify-public playlist-modify-private'
        ))
        
        # Get user ID
        user_id = sp.current_user()['id']
        
        # Create empty playlist
        playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_name,
            public=True,
            description=playlist_description
        )
        
        # Add tracks to playlist
        # Spotify API has a limit of 100 tracks per request
        for i in range(0, len(tracks), 100):
            batch = tracks[i:i + 100]
            sp.playlist_add_items(playlist['id'], batch)
            
        print(f"Successfully created playlist: {playlist_name}")
        return playlist
        
    except spotipy.SpotifyException as e:
        print(f"Error creating playlist: {str(e)}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

def search_and_add_tracks(search_terms):
    """
    Search for tracks and return their Spotify URIs
    
    Args:
        search_terms (list): List of strings to search for
        
    Returns:
        list: List of Spotify track URIs
    """
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='playlist-modify-public playlist-modify-private'
        ))
        
        track_uris = []
        for term in search_terms:
            result = sp.search(q=term, type='track', limit=1)
            if result['tracks']['items']:
                track_uris.append(result['tracks']['items'][0]['uri'])
                
        return track_uris
        
    except Exception as e:
        print(f"Error searching for tracks: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    # List of songs to search for
    songs_to_add = [
        "Sweet Child O' Mine Guns N Roses",
        "Bohemian Rhapsody Queen",
        "Stairway to Heaven Led Zeppelin"
    ]
    
    # Search for tracks and get their URIs
    track_uris = search_and_add_tracks(songs_to_add)
    
    if track_uris:
        # Create the playlist with the found tracks
        playlist = create_spotify_playlist(
            playlist_name="My Awesome Playlist",
            playlist_description="Created using Python and Spotipy",
            tracks=track_uris
        )

'''
SPOT_CLIENT_ID
SPOT_CLIENT_SECRET
SPOT_REDIRECT_URI
'''
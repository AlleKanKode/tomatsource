import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values,load_dotenv
import os
import json
import sys

def create_spotify_playlist(playlist_name, playlist_description, tracks, sp):
    """Creates a Spotify playlist and adds tracks."""
    try:
        user_id = sp.current_user()['id']
        playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_name,
            public=True,
            description=playlist_description
        )
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

def read_tracks_from_json(filename):
    """Reads track info from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # Handle potential encoding issues
            data = json.load(f)
            tracks = []
            for item in data:
                tracks.append({
                    "artist": item.get("artist"), # Use .get() to avoid KeyError if key is missing
                    "title": item.get("title")
                })
            return tracks
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during JSON reading: {e}")
        return []

def search_tracks_by_info(tracks, sp):
    """Searches for tracks based on artist and title."""
    track_uris = []
    for track in tracks:
        if not track['artist'] or not track['title']: # Skip if artist or title is missing
            print("Skipping track due to missing artist or title information")
            continue
        search_term = f"{track['artist']} {track['title']}"
        try:
            result = sp.search(q=search_term, type='track', limit=1)
            if result['tracks']['items']:
                track_uris.append(result['tracks']['items'][0]['uri'])
            else:
                print(f"No track found for: {search_term}")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify API error during search: {e}")
            continue # Continue to the next search even if one fails
        except Exception as e:
            print(f"An unexpected error occurred during track search: {e}")
            continue
    return track_uris

if __name__ == "__main__":
    load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")  # Replace with your client ID
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")  # Replace with your client secret
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")  # Replace with your redirect URI
    tracks_file = '/Users/micped/allekankode/tomatsource/episode-projekter/juleplayliste/mipede/radio_soft_playlist_20241221_225614.json'  # Replace with your JSON file path

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope='playlist-modify-public playlist-modify-private user-read-private' # Added user-read-private
        ))

        tracks_info = read_tracks_from_json(tracks_file)
        if not tracks_info:
          sys.exit(1)

        track_uris = search_tracks_by_info(tracks_info, sp)
        if not track_uris:
            print("No tracks found to add to the playlist.")
            sys.exit(1)

        playlist = create_spotify_playlist(
            playlist_name="My Playlist from JSON",
            playlist_description="Created using Python and Spotipy",
            tracks=track_uris,
            sp=sp
        )
        if not playlist:
            sys.exit(1)

    except Exception as e:
        print(f"A top-level error occurred: {e}")
        sys.exit(1)
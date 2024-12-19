'''
Denne fil er oprindeligt skabt af Claude.ai ved at jeg har spurgt claude om :
- A python script that uploads a list of songs as a playlist to Apple Music
- Se appleUp.md filen for Claude.ai's respons
'''

from dotenv import dotenv_values, load_dotenv
import requests
import os
from applemusicpy import AppleMusic

class AppleMusicPlaylistUploader:
    def __init__(self, developer_token, user_token):
        """
        Initialize the Apple Music uploader with authentication tokens.
        
        :param developer_token: JWT token for Apple Music API authentication
        :param user_token: User-specific token for accessing their Apple Music account
        """
        self.apple_music = AppleMusic(developer_token, user_token)
    
    def search_song(self, song_name, artist_name):
        """
        Search for a song on Apple Music.
        
        :param song_name: Name of the song
        :param artist_name: Name of the artist
        :return: Song ID if found, None otherwise
        """
        try:
            search_result = self.apple_music.search(song_name, types=['songs'], limit=1)
            
            if search_result and 'songs' in search_result and search_result['songs']['data']:
                # Check if the artist name matches
                for song in search_result['songs']['data']:
                    if artist_name.lower() in song['attributes']['artistName'].lower():
                        return song['id']
            
            return None
        except Exception as e:
            print(f"Error searching for song {song_name} by {artist_name}: {e}")
            return None
    
    def create_playlist(self, playlist_name, description=''):
        """
        Create a new playlist in Apple Music.
        
        :param playlist_name: Name of the playlist
        :param description: Optional description for the playlist
        :return: Playlist ID
        """
        try:
            playlist = self.apple_music.create_playlist(playlist_name, description)
            return playlist['id']
        except Exception as e:
            print(f"Error creating playlist: {e}")
            return None
    
    def add_songs_to_playlist(self, playlist_id, songs):
        """
        Add songs to a playlist.
        
        :param playlist_id: ID of the playlist
        :param songs: List of tuples (song_name, artist_name)
        :return: Number of songs successfully added
        """
        successful_adds = 0
        
        for song_name, artist_name in songs:
            song_id = self.search_song(song_name, artist_name)
            
            if song_id:
                try:
                    self.apple_music.add_to_playlist(playlist_id, [song_id])
                    successful_adds += 1
                    print(f"Added: {song_name} by {artist_name}")
                except Exception as e:
                    print(f"Could not add {song_name} by {artist_name}: {e}")
            else:
                print(f"Song not found: {song_name} by {artist_name}")
        
        return successful_adds
    
    def upload_playlist(self, playlist_name, songs, description=''):
        """
        Full workflow to create and populate a playlist.
        
        :param playlist_name: Name of the playlist
        :param songs: List of tuples (song_name, artist_name)
        :param description: Optional description for the playlist
        :return: Success status
        """
        try:
            # Create playlist
            playlist_id = self.create_playlist(playlist_name, description)
            
            if not playlist_id:
                print("Failed to create playlist")
                return False
            
            # Add songs
            added_songs = self.add_songs_to_playlist(playlist_id, songs)
            
            print(f"Playlist created: {playlist_name}")
            print(f"Successfully added {added_songs} out of {len(songs)} songs")
            
            return True
        except Exception as e:
            print(f"Playlist upload failed: {e}")
            return False

# Example usage
def main():
    # Replace with your actual tokens
    DEVELOPER_TOKEN = 'your_developer_token_here'
    USER_TOKEN = 'your_user_token_here'
    
    # List of songs to upload
    songs_to_upload = [
        ('Shape of You', 'Ed Sheeran'),
        ('Blinding Lights', 'The Weeknd'),
        ('Someone You Loved', 'Lewis Capaldi')
    ]
    
    uploader = AppleMusicPlaylistUploader(DEVELOPER_TOKEN, USER_TOKEN)
    
    success = uploader.upload_playlist(
        playlist_name='My Favorite Hits', 
        songs=songs_to_upload, 
        description='A collection of recent popular songs'
    )
    
    if success:
        print("Playlist uploaded successfully!")
    else:
        print("Failed to upload playlist")

if __name__ == "__main__":
    #main()
    '''
    Sætter OS environment variabler fra .env filen 
    '''
    load_dotenv()
    print(os.getenv("DEV_TOKEN"))

    config = dotenv_values(".env")
    print (config['DEV_TOKEN'])
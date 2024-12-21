import requests
import json
from datetime import datetime
import pytz
import re

def scrape_radio_soft():
    url = "https://radioplay.dk/radio-soft/playliste/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Make the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Find all JSON objects in the page content
        json_pattern = r'{[^{]*"nowPlayingTrack[^}]*}'
        matches = re.finditer(json_pattern, response.text)
        
        # List to store all songs
        songs = []
        copenhagen_tz = pytz.timezone('Europe/Copenhagen')
        
        # Process each JSON match
        for match in matches:
            try:
                # Parse the JSON data
                track_data = json.loads(match.group(0))
                
                # Create base song entry with required fields
                song = {
                    'artist': track_data.get('nowPlayingArtist', ''),
                    'title': track_data.get('nowPlayingTrack', ''),
                    'duration': track_data.get('nowPlayingDuration', None),
                    'image_url': track_data.get('nowPlayingImage', '')
                }
                
                # Try to parse timestamp if available
                play_time_str = track_data.get('nowPlayingTime', '')
                if play_time_str and play_time_str.strip():
                    try:
                        play_time = datetime.strptime(play_time_str, '%Y-%m-%d %H:%M:%S')
                        play_time = copenhagen_tz.localize(play_time)
                        song['timestamp'] = play_time.isoformat()
                        song['time'] = play_time.strftime('%H:%M')
                    except ValueError:
                        print(f"Invalid timestamp format: {play_time_str}")
                        # Use current time as fallback
                        now = datetime.now(copenhagen_tz)
                        song['timestamp'] = now.isoformat()
                        song['time'] = now.strftime('%H:%M')
                else:
                    # Use current time if no timestamp available
                    now = datetime.now(copenhagen_tz)
                    song['timestamp'] = now.isoformat()
                    song['time'] = now.strftime('%H:%M')
                
                # Only add songs that have both artist and title
                if song['artist'] and song['title']:
                    songs.append(song)
                    print(f"Found song: {song['artist']} - {song['title']}")
            
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing track data: {e}")
                continue
        
        # Sort songs by timestamp in descending order (newest first)
        songs.sort(key=lambda x: x['timestamp'], reverse=True)
        
        # Create the final JSON structure
        output = {
            'scrape_time': datetime.now(copenhagen_tz).isoformat(),
            'station': 'Radio Soft',
            'songs': songs
        }
        
        return output
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

if __name__ == "__main__":
    # Scrape the playlist
    playlist_data = scrape_radio_soft()
    
    if playlist_data:
        # Save to file with timestamp
        filename = f"radio_soft_playlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(playlist_data, f, ensure_ascii=False, indent=2)
        print(f"\nPlaylist saved to {filename}")
        
        # Print summary
        songs = playlist_data['songs']
        if songs:
            print(f"\nFound {len(songs)} songs")
            print("\nMost recent songs:")
            for song in songs[:3]:
                print(f"{song['time']} - {song['artist']} - {song['title']}")
        else:
            print("Warning: No songs were found in the playlist!")
    else:
        print("Failed to scrape playlist")
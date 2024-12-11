import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

class RadioSoftScraper:
    def __init__(self):
        self.base_url = "https://radioplay.dk/radio-soft/playliste"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_playlist(self):
        try:
            response = requests.get(self.base_url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all song entries (you may need to adjust these selectors based on the actual HTML structure)
            songs = []
            playlist_items = soup.select('.playlist-item')  # Adjust this selector
            
            for item in playlist_items:
                try:
                    artist = item.select_one('.artist').text.strip()  # Adjust this selector
                    title = item.select_one('.title').text.strip()    # Adjust this selector
                    
                    songs.append({
                        'artist': artist,
                        'title': title,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                except AttributeError as e:
                    print(f"Error parsing song item: {e}")
                    continue
            
            return songs
        
        except requests.RequestException as e:
            print(f"Error fetching the playlist: {e}")
            return []

    def save_to_csv(self, songs, filename='radio_soft_playlist.csv'):
        if not songs:
            print("No songs to save.")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['artist', 'title', 'timestamp'])
                writer.writeheader()
                writer.writerows(songs)
                print(f"Successfully saved {len(songs)} songs to {filename}")
        
        except IOError as e:
            print(f"Error saving to CSV: {e}")

def main():
    scraper = RadioSoftScraper()
    
    # Get the songs
    print("Fetching playlist...")
    songs = scraper.get_playlist()
    
    if songs:
        print(f"Found {len(songs)} songs")
        # Print the songs
        for song in songs:
            print(f"{song['artist']} - {song['title']}")
        
        # Save to CSV
        scraper.save_to_csv(songs)
    else:
        print("No songs were found.")

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
from datetime import datetime

def scrape_radio_soft_playlist():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get("https://radioplay.dk/radio-soft/playliste/")
        
        # Wait for the playlist to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-4x7hlc-0"))
        )
        
        # Execute JavaScript to extract the playlist data
        playlist_data = driver.execute_script("""
            const tracks = document.querySelectorAll('.sc-4x7hlc-0');
            return Array.from(tracks).map(track => ({
                title: track.querySelector('.WKFDT').textContent.trim(),
                artist: track.querySelector('.leqdTk').textContent.trim(),
                time_played: track.querySelector('.czIWjV').textContent.trim()
            }));
        """)
        
        return json.dumps(playlist_data, ensure_ascii=False, indent=2)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    playlist_json = scrape_radio_soft_playlist()
    print(playlist_json)
    
    # Optionally, save to a file
    with open(f"radio_soft_playlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w", encoding="utf-8") as f:
        f.write(playlist_json)
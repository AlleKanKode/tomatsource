from pydoc import classify_class_attrs
from bs4 import BeautifulSoup
import pprint
import requests


base_url = "https://radioplay.dk/radio-soft/playliste"
snyde_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

response = requests.get(base_url, headers=snyde_headers)
response.raise_for_status() # Det gør man tit fordi hvis der opstår en fejl så vises den her

soup = BeautifulSoup(response.text, 'html.parser')

element = soup.find_all(class_="sc-4x7hlc-0 bTBzQR")
#element = soup.select(".sc-4x7hlc-0")
print(element.__len__())

# print (type(soup))
# print (soup.prettify())

#pprint.pprint(response.text)

# print (response.text)
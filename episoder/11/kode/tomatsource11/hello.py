from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://allekankode.dk'
    response = requests.get(url)
    response.raise_for_status()
            
    soup = BeautifulSoup(response.text, 'html.parser')
    titel = soup.find('h1')

    print(titel.getText())

if __name__ == "__main__":
    main()

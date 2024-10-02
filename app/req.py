import requests
from bs4 import BeautifulSoup

params = {
    'q': 'cat'
}

response = requests.get('https://www.google.com/search', params=params)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', href=True)

# Extract and print the first 4 links
for link in links[:8]:
    print(link['href'])
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

async def get_search():
    search_query = 'cat'
    results = DDGS().text(
        keywords=search_query,
        region='wt-wt',
        safesearch='off',
        max_results=3
    )

    for result in results:
        url = result['href']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        result['body'] = text.strip()

#print(results)
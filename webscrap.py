from bs4 import BeautifulSoup
import requests


def search_wikipedia(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srprop": "",
        "utf8": ""
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "query" in data and "search" in data["query"]:
            search_results = data["query"]["search"]
            if search_results:
                page_id = search_results[0]["pageid"]
                return get_wikipedia_page(page_id)
    return None

def get_wikipedia_page(page_id):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": "",
        "explaintext": "",
        "pageids": page_id
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "query" in data and "pages" in data["query"]:
            pages = data["query"]["pages"]
            if pages:
                first_page = next(iter(pages.values()))  # Get the first page
                content_text = first_page["extract"]
                return content_text
    return None

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for element in soup(["sup", "table", "style"]):
        element.decompose()
    text = soup.get_text(separator="\n")
    return text


# query = input('enter: ',)
# response = search_wikipedia(query)
# print('response: ',response)

# question = input('enter', )
# keywords = ['what', 'who', 'whom', 'whose', 'which', 'when', 'where', 'why', 'how']
# if any(keyword in question.lower() for keyword in keywords):
#     print('yes')
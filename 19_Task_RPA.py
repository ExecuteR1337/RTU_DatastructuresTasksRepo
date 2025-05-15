import requests
from bs4 import BeautifulSoup

def rpa_nyt_trending_news():
    url = "https://www.nytimes.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for tag in soup.find_all("h2"):
        title = tag.get_text(strip=True)
        if len(title) > 30 and title not in headlines:
            headlines.append(title)

    print("Top 5 NYT Headlines:")
    for i, title in enumerate(headlines[:5], 1):
        print(f"{i}. {title}")

if __name__ == "__main__":
    rpa_nyt_trending_news() #by B. Nazarzoda 241ADB013
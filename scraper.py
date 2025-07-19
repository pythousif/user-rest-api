import requests
from bs4 import BeautifulSoup

# 1. News website ka URL
url = 'https://www.bbc.com/news'  # You can try NDTV or Times of India too

# 2. Send request
response = requests.get(url)

# 3. Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 4. Find headline tags (adjust h2/h3/a/title as per site)
headlines = soup.find_all(['h1', 'h2', 'h3'])

# 5. Save to file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            file.write(text + '\n')

print("✅ Headlines saved to headlines.txt")

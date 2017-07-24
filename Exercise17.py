import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
r = requests.get(url)
raw_html = r.text
soup = BeautifulSoup(raw_html, "html.parser")
for heading in soup.find_all(class_="story-heading"):
    if heading.a:
        print(heading.a.text.replace("\n", " ").strip())
    else:
        print(heading.contents[0].strip())

import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://en.wikipedia.org/wiki/Fauna_of_Ireland").content
soup = BeautifulSoup(html, features="html.parser")

listPattern = re.compile(r'\w*list\w*ireland', re.I)
base_url = "https://en.wikipedia.org"
list_of_links = []

for link in soup.find_all("a"):
    if link.get('href') is not None:
        match = listPattern.search(link.get('href'))
        if match:
            list_of_links.append(link.get('href'))

for link in list_of_links:
    print(base_url + link)
"""Retrieve details of animals native to Ireland from Wikipedia.

This script is intended to fetch summaries and pictures of animals for a personal project
as well as to practice webscraping and RegEx in Python."""

import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://en.wikipedia.org/wiki/Fauna_of_Ireland").content
soup = BeautifulSoup(html, features="html.parser")

listPattern = re.compile(r'\w*list\w*ireland$', re.I)
base_url = "https://en.wikipedia.org"
list_of_links = []

for link in soup.find_all("a"):
    if link.get('href') is not None:
        linkStub = link.get('href')
        match = listPattern.search(linkStub)

        if match:
            if list_of_links.count(linkStub) == 0:
                list_of_links.append(link.get('href'))

for link in list_of_links:
    print(base_url + link)
    pass

print(len(list_of_links))
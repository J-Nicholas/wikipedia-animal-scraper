"""Retrieve details of animals native to Ireland from Wikipedia.

This script is intended to fetch summaries and pictures of animals for a personal project
as well as to practice webscraping and RegEx in Python."""

import requests
from bs4 import BeautifulSoup
import re
import time
import sys

html = requests.get("https://en.wikipedia.org/wiki/Fauna_of_Ireland").content
soup = BeautifulSoup(html, features="html.parser")

# Main index page of all wildlife found in Ireland
listPattern = re.compile(r'\w*list\w*ireland$', re.I)
base_url = "https://en.wikipedia.org"
list_of_links = []

for link in soup.find_all("a"):
    linkStub = link.get('href')
    if linkStub is not None:
        match = listPattern.search(linkStub)

        if match and list_of_links.count(linkStub) == 0:
            list_of_links.append(link.get('href'))


sub_list_pattern = re.compile(r"/wiki/(?!\w*Template)\w*$")

# Each link is a list of that specific category of animal
for linkStub in list_of_links:
    page_html = requests.get(base_url + linkStub).content
    soup = BeautifulSoup(page_html, features="html.parser")
    print(soup.h1.text)
    # removes table of contents and navboxes from soup
    unwanted = soup.findAll(class_=["toc", "selected", "navbox", "portal"])
    for item in unwanted:
        item.extract()

    # get all sub-lists
    for unordered_list in soup.find_all("ul"):
        anchors = unordered_list.find_all('a')
        for anchor in anchors:
                linkStub = anchor.get("href")
                if linkStub is not None:
                    match = sub_list_pattern.match(linkStub)
                    if match:
                        print(linkStub)
    # print(group)

    # sys.exit()
    time.sleep(1)    # wikipedia asks that webscrapers only request pages once a second


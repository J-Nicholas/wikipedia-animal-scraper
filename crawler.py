import re
import time
import sys
import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"
generic_species_links = []
specific_species_links = []

def get_generic_species():
    html = requests.get("https://en.wikipedia.org/wiki/Fauna_of_Ireland").content
    soup = BeautifulSoup(html, features="html.parser")

    # Main index page of all wildlife found in Ireland
    listPattern = re.compile(r'\w*list\w*ireland$', re.I)

    for link in soup.find_all("a"):
        linkStub = link.get('href')
        if linkStub is not None:
            match = listPattern.search(linkStub)

            if match and linkStub not in generic_species_links:
                generic_species_links.append(linkStub)

def get_specific_species():
    sub_list_pattern = re.compile(r"/wiki/(?!\w*Template)(?!\w*List)\w*$", re.I)

    # Each link is a list of that specific category of animal
    for linkStub in generic_species_links:
        page_html = requests.get(base_url + linkStub).content
        soup = BeautifulSoup(page_html, features="html.parser")
        # print("\n" + soup.h1.text)
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
                        if match and linkStub not in specific_species_links:
                            specific_species_links.append(linkStub)
                            # print(linkStub)
        time.sleep(1)    # wikipedia asks that webscrapers only request pages once a second

def get_info():
    # get name, description and image for each animal
    for linkStub in specific_species_links:
        html = requests.get(base_url + linkStub)
        description = html.text.split("Contents")
        soup = BeautifulSoup(description[0], features="html.parser") # [0] is first half before table of contents
        info_box = soup.find(class_="infobox")
        unwanted = info_box.findAll(name="p")

        for item in unwanted:
            item.extract()

        for paragraph in soup.findAll("p"):
            print(paragraph.text)

        time.sleep(1)

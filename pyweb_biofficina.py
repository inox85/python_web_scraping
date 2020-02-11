import urllib2
from lxml import html
import requests
from bs4 import BeautifulSoup
import sys

response = urllib2.urlopen("https://www.ecco-verde.it/viso")
links_page = response.read()
soup = BeautifulSoup(links_page, 'html.parser')

links = soup.find_all("div", {"class": "product__title"})

for link in links:
    part_link = link.find("a").get("href")
    total_link = "https://www.ecco-verde.it/" + part_link
    print(total_link)

for page in range(1,166):
    payload = { 'page': page }
    url = "https://www.ecco-verde.it/viso"
    response = requests.post(url, data=payload)
    #response = urllib2.urlopen("https://www.ecco-verde.it/viso?page=" + str(page))
    
    links_page = response.read()
    soup = BeautifulSoup(links_page, 'html.parser')
    for link in links:
        part_link = link.find("a").get("href")
        total_link = "https://www.ecco-verde.it/" + part_link
        print(total_link)





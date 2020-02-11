import urllib2
from lxml import html
import requests
from bs4 import BeautifulSoup
import sys

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list:
            final_list.append(num) 
    return final_list 

def clean_file(source_file, dest_file):
    lines_seen = set() # holds lines already seen
    outfile = open("aroma_zone_link.txt", "w")
    count = 0
    count_total = 0
    for line in open("aroma_zone_link_clean.txt", "r"):
        count_total += 1
        if line not in lines_seen: # not a duplicate
            count += 1
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print("Record totali: " + str(count_total))
    print("Record rimasti: " + str(count))


response = urllib2.urlopen("https://www.aroma-zone.com/tous-nos-produits/extraits-naturels.html")
links_page = response.read()
soup = BeautifulSoup(links_page, 'html.parser')
f_link = open("aroma_zone_link.txt" , "w+")
f_prod = open("aroma_zone_prod.txt" , "w+")

temp_links = soup.find_all('a')

links = Remove(temp_links)

pages = len(links)

prev_url = ""

for link in links:
    if "www" in link.get('href'):
        f_link.write(link.get('href') + "\n")

print("Trovate " + str(pages) + " pagine")
count = 0
for link in soup.find_all('a'):
    if "www" in link.get('href'):
        count += 1
        print(str(count) + "/" + str(pages) + " - " + str(count/pages) + "%")
        print(link.get('href')+"\n")
        url = link.get('href')+"\n"
        try:
            response = urllib2.urlopen(url)
        except:
            print("Errore caricamento pagina")
        #response = urllib2.urlopen("https://www.aroma-zone.com/info/fiche-technique/fleurs-hibiscus-bio-aroma-zone")
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        name = soup.find("h1", {"itemprop": "name"})
        prices = soup.find("span", {"class": "price"})
        string = ""
        if url != prev_url:
            try:
                for c in range(len(name.contents)):
                    print(name.contents[c].rstrip())
                    string += name.contents[c].rstrip() + ";"

                for c in range(len(prices.contents)):
                    print(prices.contents[c].rstrip())
                    string += prices.contents[c].rstrip() + ";"
                    string += link.get('href').rstrip()
        
                    f_prod.write(string.encode("utf-8").rstrip() + "\n")
            except Exception,e:
                print(e)
                print("Nessun contenuto")
        else:
            print("Url ripetuto")
        prev_url = url


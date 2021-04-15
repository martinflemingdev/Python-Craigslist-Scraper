import requests
import pprint
from bs4 import BeautifulSoup

# declare variable for target URL and use requests library to perform GET
freeURL = 'https://philadelphia.craigslist.org/d/free-stuff/search/zip'
freePage = requests.get(freeURL)

musicURL = 'https://philadelphia.craigslist.org/search/msa?'
musicPage = requests.get(musicURL)

# instantiates BeautifulSoup object that is the page HTML content of the URL
freeSoup = BeautifulSoup(freePage.content, features="html.parser")
musicSoup = BeautifulSoup(musicPage.content, features="html.parser")

# can declare variable to hold specific DOM element id's with soup.find(id="id_name")
# can declare variable to hold all class elements with soup.find_all(class_='class_name')
freeResults = freeSoup.find_all('div', class_="result-info")
musicResults = musicSoup.find_all('div', class_="result-info")

# using for loop to check if header link text includes 'keyboard' or 'synthesizer'
# if it does, print the item's name, price, location, and URL

print('FREE SECTION:\n')

for free in freeResults:
    item = free.find('a', class_="result-title hdrlnk")
    if "keyboard" in item.string.lower() or "synthesizer" in item.string.lower():
        link = free.find('a')['href']
        price = free.find(class_='result-price')
        hood = free.find(class_='result-hood')
        print(item.text)
        print(price.text)
        print(hood.text)
        print(f"Buy here: {link}\n")

print('MUSIC SECTION:\n')

for i in musicResults:
    item = i.find('a', class_="result-title hdrlnk")
    if "keyboard" in item.string.lower() or "synthesizer" in item.string.lower():
        link = i.find('a')['href']
        price = i.find(class_='result-price')
        hood = i.find(class_='result-hood')
        print(item.text)
        print(price.text)
        print(hood.text)
        print(f"Buy here: {link}\n")

# possible use of anonymous lambda function to filter before for loop
# keyz = musicResults.find_all('a', string=lambda text: "keyboard" or "synthesizer" in text.lower())

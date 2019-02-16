from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

countbr = 0
countp = 0
countlink = 0

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.findAll('br'):
    countbr = countbr + 1
for link in soup.findAll('p'):
    countp = countp + 1
for link in soup.findAll('a', href=True):
    countlink = countlink + 1

print('Links: ', countlink)
print('Spaces: ', countbr + countp)

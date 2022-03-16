from bs4 import BeautifulSoup
import requests
import os
 
r = requests.get("https://www.larvalabs.com/cryptopunks/sales?perPage=96&page=2")

soup = BeautifulSoup(r.text, "html.parser")

images = soup.find_all('img')

print(len(images))

count = 0

for image in images:
    name = image['alt']
    link = image['src']
    
    with open(name.replace(' ', '-').replace('/', '') + '.png', 'wb') as f:
        print(len(images) - images.index(image))
        index = images.index(image)
        print(index)
        print("https://www.larvalabs.com" + link)
        im = requests.get("https://www.larvalabs.com" + link)
        f.write(im.content)


# pixelated
# print(name, "https://www.larvalabs.com" + link)
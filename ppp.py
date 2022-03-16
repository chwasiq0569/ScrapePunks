from bs4 import BeautifulSoup
import requests
import os
 
perPage = 96
page = 1
downloadedPerPage = 0

def makeRequest(url):
  r = requests.get(url)

  soup = BeautifulSoup(r.text, "html.parser")

  images = soup.find_all('img')

  return images

makeRequest(f"https://www.larvalabs.com/cryptopunks/sales?perPage={str(perPage)}&page={str(page)}")

def downloadImages(downloadedPerPage, images, page, perPage):
  for image in images:
    name = image['alt']
    link = image['src']
    print("len(images)" + str(len(images)))

    if downloadedPerPage < len(images):
        downloadedPerPage = downloadedPerPage + 1
        print("downloads" + str(downloadedPerPage))
        
    with open(name.replace(' ', '-').replace('/', '') + '.png', 'wb') as f:
        print(len(images) - images.index(image))
        index = images.index(image)
        print(index)
        print("https://www.larvalabs.com" + link)
        im = requests.get("https://www.larvalabs.com" + link)
        f.write(im.content)


def main(downloadedPerPage, perPage):
  for i in range(214):
    if i > 108:
    # if downloadedPerPage == 96 or page == 1:
      images = makeRequest(f"https://www.larvalabs.com/cryptopunks/sales?perPage={str(perPage)}&page={str(i)}")
      print(len(images))
      downloadImages(downloadedPerPage, images, i, perPage)
      print("page" + str(i+1))
      print(f"https://www.larvalabs.com/cryptopunks/sales?perPage={str(perPage)}&page={str(i)}")

  # if downloadedPerPage == 95:
  #   downloadedPerPage=0
  #   main(downloadedPerPage, page, perPage)

main(downloadedPerPage, perPage)
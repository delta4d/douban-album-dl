from bs4 import BeautifulSoup
import requests

class Album:
    BASE_URL = "https://www.douban.com/photos/album/"

    def __init__(self, album_id):
        self.url = Album.BASE_URL + album_id + "/?start="

    def photos(self):
        start = 0
        while True:
            next_photos = self.__photos(start)
            step = len(next_photos)
            if 0 == step:
                break
            for photo in next_photos:
                yield photo.img["src"].replace("photo/lthumb", "photo/large")
            start += step

    def __photos(self, start):
        url = self.url + str(start)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all("div", class_="photo_wrap")

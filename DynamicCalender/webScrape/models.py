from django.db import models
import requests
from bs4 import BeautifulSoup
# Create your models here.

list_of_websites = ["https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen", "https://www.timeshighereducation.com/", "https://skift.com/"]


def web_scrape(website):
    url = website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find("div", {"class": "lBwEZb BL5WZb GndZbb"})
    for link in div:
        article_link = link.find('a')['href']
        print(article_link)
        title_class = link.find("a", {"class": "DY5T1d RZIKme"})
        title = title_class.text.strip()
        print(title)
        img = link.find("img", {"class": "tvs3Id QwxBBf"})
        img_link = img["src"]
        print(img_link)
        
class Article(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField()
    image = image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title
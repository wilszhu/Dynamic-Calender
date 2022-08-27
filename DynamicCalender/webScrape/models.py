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
        print(link.find('a')['href'])
        

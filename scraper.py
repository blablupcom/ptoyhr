import sys
import requests
from bs4 import BeautifulSoup as bs
import re
from mutagen.mp3 import MP3
from urllib import urlretrieve
import json
import math
import itertools
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
import time


def categories_scrape(base_url):
    page = requests.get(base_url)
    soup = bs(page.text, 'lxml')
    links = soup.find_all('a')
    print links
    
    
    
if __name__ == '__main__':
    #
    # initials = ['http://www.soundboard.com/category/Science-Nature', 'http://www.soundboard.com/category/Games',
    # 'http://www.soundboard.com/category/Television', 'http://www.soundboard.com/category/Sound-Effects',
    # 'http://www.soundboard.com/category/Movies']
    initials = 'http://www.dailywav.com//archives/shows'
    categories_scrape(initials)
    

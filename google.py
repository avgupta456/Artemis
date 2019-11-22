from googlesearch import search
import re

import requests
from bs4 import BeautifulSoup

KEY_file = open('key.txt', 'r')
KEY=KEY_file.readlines()[0]

pause = 0.1

def GS(query, count=10):
    results = []
    for i in search(query=query, tld='co.in', lang='en',
            num=count, stop=count, pause=pause):
        results.append(i)
    return results

def GS_site(query, site, count=10):
    results = GS(query, count)
    out = []

    for i in range(len(results)):
        if re.search(site, results[i]) != None:
            out.append(results[i])

    return out

def printArr(results):
    for i in range(len(results)):
        print(results[i])

def getHTML(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def GS_HTML(query):
    results = GS(query, 1)
    return getHTML(results[0])

def GS_HTML_site(query, site):
    results = GS_site(query, site, 5)
    return getHTML(results[0])

def getElements(html, object, attrs):
    arr = []
    for obj in html.find_all(object, attrs=attrs):
        arr.append(obj.text)
    return arr

def GS_elements(query, object, attrs):
    html = GS_HTML(query)
    return getElements(html, object, attrs)

def GS_elements_site(query, site, object, attrs):
    html = GS_HTML_site(query, site)
    return getElements(html, object, attrs)

city = "New York City"
query = "TripAdvisor" + city
site = "https://www.tripadvisor.com/Tourism"
object = "span"
attrs = {'class', 'social-shelf-items-ShelfLocationSection__name--CdA_A'}

printArr(GS_elements_site(query, site, object, attrs))

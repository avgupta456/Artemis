from googlesearch import search
import re

import requests
from bs4 import BeautifulSoup

KEY_file = open('key2.txt', 'r')
KEY=KEY_file.readlines()[0]

pause = 0.0

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

def getHTML_all(URLs):
    soups = []
    for URL in URLs:
        soups.append(BeautifulSoup(requests.get(URL).content, 'html5lib'))

    return soups

def GS_HTML(query):
    results = GS(query, 1)
    return getHTML(results[0])

def GS_HTML_site(query, site):
    results = GS_site(query, site, 5)
    return getHTML(results[0])

def GS_HTML_all(query):
    results = GS(query, 10)
    return getHTML_all(results)

def GS_HTML_site_all(query, site):
    results = GS_site(query, site, 10)
    return getHTML_all(results)

def getElements(html, object, attrs):
    arr = []
    for obj in html.find_all(object, attrs=attrs):
        arr.append(obj.text)
    return arr

def getElements_all(htmls, object, attrs):
    unique = set([])
    for html in htmls:
        for obj in html.find_all(object, attrs=attrs):
            unique.add(obj.text)

    arr = []
    for i in unique:
        arr.append(i)

    return arr

def GS_elements(query, object, attrs):
    html = GS_HTML(query)
    return getElements(html, object, attrs)

def GS_elements_site(query, site, object, attrs):
    html = GS_HTML_site(query, site)
    return getElements(html, object, attrs)

def GS_elements_all(query, objects, attrs):
    htmls = GS_HTML_all(query)
    return getElements_all(htmls, object, attrs)

def GS_elements_site_all(query, site, object, attrs):
    htmls = GS_HTML_site_all(query, site)
    return getElements_all(htmls, object, attrs)

def tripAdvisorTourism(city):
    query = "TripAdvisor" + city
    site = "https://www.tripadvisor.com/Tourism"
    object = "span"
    attrs = {'class', 'social-shelf-items-ShelfLocationSection__name--CdA_A'}

    places = GS_elements_site_all(query, site, object, attrs)
    return places

def tripAdvisorAttractions(city):
    query = "TripAdvisor" + city
    site = "https://www.tripadvisor.com/Attractions"
    object = "a"
    attrs = {'class', 'attractions-attraction-overview-pois-PoiInfo__name--SJ0a4'}

    places = GS_elements_site_all(query, site, object, attrs)
    return places

def tripAdvisorCategory(city, category):
    query = "TripAdvisor" + city + " " + category
    site = "https://www.tripadvisor.com/Attractions"
    object = "div"
    attrs = {'class', 'listing_title'}

    places = GS_elements_site_all(query, site, object, attrs)

    new_places = []
    for place in places:
        try: new_places.append(place.split("\n")[1])
        except IndexError: pass

    return new_places

def tripAdvisor(city):
    unique = set([])
    places = tripAdvisorTourism(city)
    for place in places: unique.add(place)
    print(len(places))

    places = tripAdvisorAttractions(city)
    for place in places: unique.add(place)
    print(len(places))

    categories = ["Sights and Landmarks", "Museums", "Architectural Buildings",
        "Historic Sites", "Monuments and Statues", "Parks"]

    for category in categories:
        places = tripAdvisorCategory(city, category)
        for place in places: unique.add(place)
        print(len(places))

    return list(unique)

def tripAdvisorQuick(city):
    unique = set([])
    places = tripAdvisorTourism(city)
    for place in places: unique.add(place)
    print(len(places))

    places = tripAdvisorAttractions(city)
    for place in places: unique.add(place)
    print(len(places))

    return list(unique)

import requests

KEY_file = open('key.txt', 'r')
KEY=KEY_file.readlines()[0]


class Gsearch_python:

    def __init__(self, name_search):
        self.name = name_search

    def Gsearch(self):
        count = 0
        results = []

        try:
            from googlesearch import search
        except ImportError:
             print("No Module named 'google' Found")

        for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=10,pause=2):
            results.append(i)

        return results

from googlesearch import search

KEY_file = open('key.txt', 'r')
KEY=KEY_file.readlines()[0]

def google(query):
    results = []
    for i in search(query=query, tld='co.in', lang='en', num=10, stop=10, pause=2):
        results.append(i)
    return results

def print_google(query):
    results = google(query)
    for i in range(len(results)):
        print(results[i])

print_google("New England Patriots")

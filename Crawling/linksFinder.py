from bs4 import BeautifulSoup as bs
import requests as req
def getResponse(url):
    try:
        response = req.get(url)
    except:
        return None
    return response
def findLinks(htmlDoc):
    soup = bs(htmlDoc)
    return soup.find_all('a')
def extractLinks(url):
    response = getResponse(url)
    link = findLinks(response.text)
    links = [li.get('href').encode('utf-8') for li in link if ('#' not in li.get('href')) and not ('extiw' == li.get('class')) and '.org' not in li.get('href')]
    return links
mainUrl = 'https://fa.wikipedia.org'
url = 'https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
extractLinks(url)
import requests as req
from bs4 import BeautifulSoup as bs
class crawler:
    def start():
        pass
    @staticmethod
    def getResponse(url):
        try:
            response = req.get(url)
        except:
            return None
        return response
    
class dataExtractor(crawler):
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self):
        pass
    def loadLinks(self,urlAddr):
        with open(urlAddr,'r') as file:
            self.links = file.read()
        return self.links
    def getCorpus(self,soup):
        corpus = soup.find_all('p')
        return corpus
    def getImages(self,soup):
        images = soup.find_all('img')
        return images
    def getHeader(self,soup):
        headers = soup.find_all('span',attrs={'class':'mw-headline'})
        return headers
'''       links extractor class       '''
class linksExtractor(crawler):
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self,numLinks = None):
        links = []
        links.extend(self.extractLinks(''))
        for link in links:
            pageLinks = self.extractLinks(link)
            if pageLinks == None:
                continue
            if not numLinks == None:
                if numLinks <= len(links):
                    return links[:numLinks]
            links.extend(link)
    def findLinks(self,htmlDoc):
        soup = bs(htmlDoc,'html.parser')
        return soup.find_all('a')
    def extractLinks(self,url):
        url = self.mainUrl + url
        response = self.getResponse(url)
        if response == None:
            return None
        link = self.findLinks(response.text)
        links = []
        for li in link:
            try:
                href = str(li.get('href'))
            except:
                continue
            if ('#' not in href) and not ('extiw' == li.get('class')) and '.org' not in href:
                links.append(href)
        return links
    @staticmethod
    def saveLinks(links,addr):
        with open(addr,'w') as file:
            file.write('\n'.join(links))
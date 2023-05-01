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
    @staticmethod
    def save(List,addr):
        with open(addr,'w',encoding='utf-8') as file:
            file.write('\n'.join(List))
class dataExtractor(crawler):
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self,links,numPages = 10):
        corpus = []
        headers = []
        images = []
        for i,link in enumerate(links):
            response = self.getResponse(self.mainUrl + link)
            if response == None:
                continue
            soup = bs(response.text,'html.parser')
            corp = self.getCorpus(soup=soup)
            corpus.extend(corp) if not corp == None else None  
            header = self.getHeader(soup=soup)
            headers.extend(header) if not header == None else None
            image = self.getImages(soup=soup)
            images.extend(image) if not image == None else None
            if i == numPages:
                break
        return [corpus,images,headers]
            
    def loadLinks(self,urlAddr):
        with open(urlAddr,'r') as file:
            self.links = file.read()
        return self.links
    def getCorpus(self,soup):
        corpus = soup.find_all('p')
        corpus = [c.text for c in corpus]
        return corpus
    def getImages(self,soup):
        images = soup.find_all('img')
        images = [img.get('src') for img in images]
        return images
    def getHeader(self,soup):
        headers = soup.find_all('span',attrs={'class':'mw-headline'})
        headers = [h.text for h in headers]
        return headers
'''       links extractor class       '''
class linksExtractor(crawler):
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self,numLinks = None):
        links = []
        linksLen = 0
        links.extend(self.extractLinks(''))
        for link in links:
            pageLinks = self.extractLinks(link)
            if pageLinks == None:
                continue
            if type(link) == type(''):
                links.append(link)
                linLen = 1
            else:
                linLen = len(link)
                links.extend(link)
            linksLen += linLen
            if not numLinks == None:
                if numLinks <= linksLen:
                    return links[:numLinks]
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

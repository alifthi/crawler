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
            file.write(List)
    def saveAsJson(self,List,addr):
        import json
        with open(addr,'w',encoding='utf-8') as file:
            json.dump(self.makedictionary(*List),file,indent=6)
    @staticmethod
    def makedictionary(url,corpus,headers,imageLinks):
        jsonDict = {}
        for i,u in enumerate(url):
            jsonDict.update({u:{'corpus':corpus[i],'header':headers[i],'imageLinks':imageLinks[i],'flag':False}})
        return jsonDict
class dataExtractor(crawler):
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self,links):
        corpus = []
        headers = []
        images = []
        for link in links:
            response = self.getResponse(self.mainUrl + link)
            if response == None:
                continue
            soup = bs(response.text,'html.parser')
            contentDivTags = soup.find('div',attrs={'id':'mw-content-text'})
            if contentDivTags == None:
                continue
            corp = self.getCorpus(soup=contentDivTags)
            corpus.extend(corp) if not corp == None else None  
            header = self.getHeader(soup=contentDivTags)
            headers.append(header)
            image = self.getImages(soup=contentDivTags)
            images.append(image)
        return [corpus,images,headers]
            
    def loadLinks(self,urlAddr):
        with open(urlAddr,'r') as file:
            self.links = file.readlines()
        return self.links
    def getCorpus(self,soup):
        corpus = soup.find_all('p')
        corpus = [c.text for c in corpus]
        return corpus
    def getImages(self,soup):
        images = soup.find_all('img')
        imageLinks = ''
        for img in images: imageLinks = imageLinks + img.get('src') + '\n' 
        return imageLinks
    def getHeader(self,soup):
        headers = soup.find_all('span',attrs={'class':'mw-headline'})
        header = ''
        for h in headers: header = header + h.text + '\n'
        return header
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
            if type(pageLinks) == type(''):
                links.append(pageLinks)
                linLen = 1
            else:
                linLen = len(pageLinks)
                links.extend(pageLinks)
            linksLen += linLen
            if not numLinks == None:
                if numLinks <= linksLen:
                    return links[:numLinks]
    def findLinks(self,soup):
        return soup.find_all('a')
    def extractLinks(self,url):
        url = self.mainUrl + url
        response = self.getResponse(url)
        if response == None:
            return None
        soup = bs(response.text,'html.parser')
        contentDivTags = soup.find('div',attrs={'id':'mw-content-text'})    
        for tag in contentDivTags.find_all('span',attrs={'mw-editsection'}): tag.decompose()
        link = self.findLinks(contentDivTags)
        links = []
        for li in link:
            try:
                href = str(li.get('href'))
            except:
                continue
            if ('#' not in href) and not ('extiw' == li.get('class')) and '.org' not in href:
                links.append(href)
        return links
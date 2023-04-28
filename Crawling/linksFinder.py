from bs4 import BeautifulSoup as bs
import requests as req
class linksExtractor:
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def getResponse(self,url):
        try:
            response = req.get(url)
        except:
            return None
        return response
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
from bs4 import BeautifulSoup as bs

class dataExtractor:
    def __init__(self,mainUrl) -> None:
        self.mainUrl = mainUrl
    def start(self):
        pass
    def loadLinks(self,urlAddr):
        with open(urlAddr,'r') as file:
            self.links = file.read()
        return self.links
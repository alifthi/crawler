from bs4 import BeautifulSoup as bs
import requests as req
def getResponse(url):
    try:
        response = req.get(url)
    except:
        return None
    return response

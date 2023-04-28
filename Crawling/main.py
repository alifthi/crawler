import sys

if __name__ == '__main__':
    mainUrl = 'https://fa.wikipedia.org'
    url = '/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
    switch = sys.argv[1]
    links = [url]
    if switch == 'extractUrl':
        from linksFinder import linksExtractor
        lEx = linksExtractor(mainUrl)
        links = lEx.start(numLinks=10)
        lEx.saveLinks(links=links,addr='./links.txt')
    elif switch == 'extractData':
        from dataExtractor import dataExtractor as extractor
        extractor = extractor(mainUrl)
        links = extractor.loadLinks('../links/links.txt')
        # for link in links:
        #     extractor.start(link)
    elif switch == 'extractOneLink':
        pass
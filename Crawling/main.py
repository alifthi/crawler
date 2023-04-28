import sys

if __name__ == '__main__':
    
    url = '/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
    switch = 'extractUrl' # sys.argv[1]
    links = [url]
    if switch == 'extractUrl':
        from linksFinder import linksExtractor
        lEx = linksExtractor('https://fa.wikipedia.org')
        links = lEx.start(numLinks=10)
        lEx.saveLinks(links=links,addr='.\\links.txt')
    elif switch == 'extractCorpus':
        from dataExtractor import dataExtractor as extractor
        extractor = extractor()
        links = extractor.loadLinks()
        for link in links:
            extractor.start(link)
    elif switch == 'extractOneLink':
        pass
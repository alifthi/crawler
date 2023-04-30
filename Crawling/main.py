import sys
if __name__ == '__main__':
    mainUrl = 'https://fa.wikipedia.org'
    url = '/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
    switch = sys.argv[1]
    links = [url]
    if switch == 'extractUrl':
        from crawler import linksExtractor
        lEx = linksExtractor(mainUrl)
        links = lEx.start(numLinks=10)
        lEx.save(links,addr='../links/links.txt')
    elif switch == 'extractData':
        from crawler import dataExtractor as extractor
        extractor = extractor(mainUrl)
        links = extractor.loadLinks('../links/links.txt')
        corpus,images,header = extractor.start(links=links) 
        extractor.save(corpus,'../corpus/corpus.txt')
        extractor.save(images,'../imageLinks.txt')
        extractor.save(header,'../header/header.txt')
    elif switch == 'extractOneLink':
        pass
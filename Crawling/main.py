import sys

if __name__ == '__main__':
    linksExtractor = linksExtractor('https://fa.wikipedia.org')
    url = '/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
    switch = sys.argv[1]
    links = [url]
    if switch == 'extractUrl':
        from linksFinder import linksExtractor
        links.append(linksExtractor.extractLinks(url))
        for link in links:
            pageLinks = linksExtractor.extractLinks(url)
            if pageLinks == None:
                continue
            links.extend(link)
    elif switch == 'extractCorpus':
        from dataExtractor import dataExtractor as extractor
        extractor = extractor()
        links = extractor.loadLinks()
        for link in links:
            extractor.start(link)
    elif switch == 'extractOneLink':
        pass
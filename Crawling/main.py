import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

if __name__ == '__main__':
    url = '/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u','--url',default='https://fa.wikipedia.org',help='crawling sites main page')
    parser.add_argument('-m','--mode',default='extractUrl',help='extraction mode')
    parser.add_argument('-n','--numOfUrl',default=None,type=int,help='number of pages that want to crawl')
    parser.add_argument('-s','--savePath',default='../crawlingData/',help='the path that you want to save data')
    parser.add_argument('-lp','--loadPath',default='../crawlingData/links/',help='links path')
    parser.add_argument('-sm','--saveMode',default='json',help='saving data mode')
    args = vars(parser.parse_args())
    mainUrl = args['url']
    savePath = args['savePath']
    loadPath = args['loadPath']
    numLinks = args['numOfUrl']
    mode = args['mode']
    saveMode = args['saveMode']
    switch = sys.argv[1]
    links = [url]
    if mode == 'extractUrl':
        from crawler import linksExtractor
        lEx = linksExtractor(mainUrl)
        links = lEx.start(numLinks=numLinks)
        lEx.save(links,addr=savePath + 'links/links.txt')
    elif mode == 'extractData':
        from crawler import dataExtractor as extractor
        extractor = extractor(mainUrl)
        links = extractor.loadLinks(loadPath + 'links.txt')
        links = links[:numLinks]
        corpus,images,header = extractor.start(links=links) 
        if saveMode == 'txt':
            extractor.save(corpus,savePath + 'corpus/corpus.txt')
            extractor.save(images,savePath + 'imageLinks/imageLinks.txt')
            extractor.save(header,savePath + 'header/header.txt')
        elif saveMode == 'json':
            extractor.saveAsJson([links,corpus,header,images],savePath + 'jsonData/Data.json')
    elif mode == 'extractOneLink':
        pass
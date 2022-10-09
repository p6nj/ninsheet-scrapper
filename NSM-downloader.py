SheetPath=r''
assert SheetPath,'Please provide the path to your sheet music root folder in the string on the line above (var SheetPath).'

from genericpath import exists
from os import chdir, mkdir
from sys import argv
from pyquery import PyQuery as pq
from requests import get

__doc__="""NinSheetMusic Downloader
usage:
    NSM-downloader [SERIE]
where SERIE is the serie name, like SuperMario, Megaman...
You can find these names in the end of the serie page  URL."""

if len(argv)!=2:print(__doc__)
else:
    chdir(SheetPath)
    url="https://www.ninsheetmusic.org/browse/series/"+argv[1]
    w=pq(url)
    url='https://www.ninsheetmusic.org'
    name=w('#mainTitle > span:nth-child(1)').text()[:-12]
    # print(name+'/')
    try:mkdir(name)
    except:pass
    chdir(name)

    i=1
    sub=True
    while True:
        i+=1
        sub=w(f'section.contentBox:nth-child({i}) > heading:nth-child(1) > div:nth-child(1)').text().split('\n')
        if len(sub)==1:break
        sub,n=tuple(sub[:2])
        print('{:<7}{} ({})'.format(i-1,sub,n))
        try:mkdir(sub)
        except:pass
        j=0
        while True:
            j+=1
            sheet=w(f'section.contentBox:nth-child({i}) > ul > li:nth-child({j}) > div:nth-child(1) > div:nth-child(1)').text().replace('/','-')
            if not sheet:break
            print('{:<7}'.format(f'{i-1}.{j}')+sheet)
            format=sub+'/'+sheet+'.pdf'
            if exists(format):continue
            download=url+w(f'section.contentBox:nth-child({i}) > ul > li:nth-child({j}) > a[title="Download PDF file (\.pdf)"]').attr['href']
            data=get(download).content
            with open(format,'wb') as f:f.write(data)
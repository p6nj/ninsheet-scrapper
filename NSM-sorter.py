from PyPDF2 import PdfFileReader
from re import search
with open("/home/breval/Documents/sheet music/ninsh/Super Mario/Luigi's Mansion 3/Main Theme.pdf",'rb') as f:
    pdf=PdfFileReader(f)
    txt=pdf._get_page(0).extract_text()
    print(search(r'q = (\d+)',txt).group(1))
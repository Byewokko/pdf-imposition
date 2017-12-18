"""
# Imposes ordered pages on a 2x3x2 sheet
"""


from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.pdf import PageObject
import sys

fname = sys.argv[1]
o = PdfFileWriter()

with open(fname,"rb") as si, open(fname[:-4]+"-sheet.pdf","wb") as so:
    i = PdfFileReader(si)
    tot = i.getNumPages()
    page = i.getPage(0)
    dims = page.bleedBox.getWidth(), page.mediaBox.getHeight()
    n = 0
    while n < tot:
        newPage = PageObject.createBlankPage(None, 2*dims[0], 3*dims[1])
        newPage.mergeTranslatedPage(i.getPage(n),0,dims[1]*2)
        newPage.mergeTranslatedPage(i.getPage(n+1),dims[0],dims[1]*2)
        newPage.mergeTranslatedPage(i.getPage(n+2),0,dims[1])
        newPage.mergeTranslatedPage(i.getPage(n+3),dims[0],dims[1])
        newPage.mergeTranslatedPage(i.getPage(n+4),0,0)
        newPage.mergeTranslatedPage(i.getPage(n+5),dims[0],0)
        o.addPage(newPage)
        n += 6

    o.write(so)

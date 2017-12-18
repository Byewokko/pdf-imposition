"""
# Reorders pages so that 2x3x2 of them fit on one large printer's sheet
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

fname = sys.argv[1]
o = PdfFileWriter()

with open(fname,"rb") as si, open(fname[:-4]+"-12.pdf","wb") as so:
    i = PdfFileReader(si)
    tot = i.getNumPages()

    n = 0
    while n < tot:
        o.addPage(i.getPage(n))
        o.addPage(i.getPage(n+1))
        if n + 4 < tot:
            o.addPage(i.getPage(n+4))
            o.addPage(i.getPage(n+5))
        else:
            o.addPage(i.getPage(n))
            o.addPage(i.getPage(n+1))
        if n + 8 < tot:
            o.addPage(i.getPage(n+8))
            o.addPage(i.getPage(n+9))
        else:
            o.addPage(i.getPage(n))
            o.addPage(i.getPage(n+1))
        o.addPage(i.getPage(n+2))
        o.addPage(i.getPage(n+3))
        if n + 6 < tot:
            o.addPage(i.getPage(n+6))
            o.addPage(i.getPage(n+7))
        else:
            o.addPage(i.getPage(n))
            o.addPage(i.getPage(n+1))
        if n + 10 < tot:
            o.addPage(i.getPage(n+10))
            o.addPage(i.getPage(n+11))
        else:
            o.addPage(i.getPage(n))
            o.addPage(i.getPage(n+1))
        n += 12

    o.write(so)

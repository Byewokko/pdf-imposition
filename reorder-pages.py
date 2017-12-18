"""
# This reorders pages to match the order of a 4-page sheet
# It's an auxiliary step
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

fname = sys.argv[1]
o = PdfFileWriter()

with open(fname,"rb") as si, open(fname[:-4]+"-4.pdf","wb") as so:
    i = PdfFileReader(si)
    tot = i.getNumPages()

    n = 0
    while n < tot:
        o.addPage(i.getPage(n+1))
        o.addPage(i.getPage(n+2))
        o.addPage(i.getPage(n+3))
        o.addPage(i.getPage(n))
        n += 4

    o.write(so)

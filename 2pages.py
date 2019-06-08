import sys

import PyPDF2 as pdf

fname = sys.argv[1]
fname = "test.pdf"
with open(fname, "rb") as pdff:
    reader = pdf.PdfFileReader(pdff)

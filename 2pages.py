import sys

import PyPDF2 as PP

fname = sys.argv[1]
#fname = "/home/m17/hruska/Downloads/1903.08855.pdf"
with open(fname, "rb") as pdfin, open(fname.replace(".pdf", ".new.pdf"), "wb") as pdfout:
    reader = PP.PdfFileReader(pdfin)
    writer = PP.PdfFileWriter()
    total = reader.getNumPages()
    page = reader.getPage(0)
    dims = page.trimBox.getWidth(), page.trimBox.getHeight()

    for i in range(0, total, 2):
        newPage = PP.pdf.PageObject.createBlankPage(None, dims[1], dims[0])
        p1 = reader.getPage(i)
        try:
            p2 = reader.getPage(i+1)
        except IndexError:
            p2 = PP.pdf.PageObject.createBlankPage(None, dims[1], dims[0])

        # Pages are shrunk by the factor of sqrt(2) minus 32/30 to crop the margins
        newPage.mergeScaledTranslatedPage(p1, 2**(-1/2)/30*33, -dims[1]/30, -dims[0]/30*2)
        newPage.mergeScaledTranslatedPage(p2, 2**(-1/2)/30*33, dims[1]/2 - dims[1]/30, -dims[0]/30*2)
        writer.addPage(newPage)

    writer.write(pdfout)


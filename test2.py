import PyPDF2

pdfName = open("WG_LoyalManager_en_1_75_1.pdf", "rb")
reder1 = PyPDF2.PdfFileReader(pdfName)

pdfNameDest = open("dest.pdf", "wb")
writer1 = PyPDF2.PdfFileWriter()

# pag_0 = reder1.getPage(0)
#
# writer1.addPage(pag_0)
# writer1.addPage(pag_0)
# writer1.addPage(pag_0)

for numpag in range(reder1.numPages):
    writer1.addPage(reder1.getPage(numpag))


writer1.write(pdfNameDest)

pdfName.close()
pdfNameDest.close()

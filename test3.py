from os import listdir

import PyPDF2
import os

listaFile = listdir()

#open output pdf destination file
pdfNameDest = open(input(), "wb")
merger = PyPDF2.PdfFileMerger()

for nomeFile in listaFile:
    if os.path.isfile(nomeFile) and nomeFile.lower().endswith(".pdf"):
        pdfFile = open(nomeFile, "rb")
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        # print(nomeFile)

merger.write(pdfNameDest)
pdfNameDest.close()
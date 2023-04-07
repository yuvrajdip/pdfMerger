import PyPDF2, os

pdfFiles = []

for fileName in os.listdir('./'):
    if fileName.endswith('.pdf') and fileName != 'merged.pdf':
        pdfFiles.append(fileName)

pdfFiles.sort( key= str.lower)

pdfMerger = PyPDF2.PdfMerger()

for fileName in pdfFiles:
    pdfMerger.append(fileName)

pdfMerger.write("merged.pdf")
pdfMerger.close()
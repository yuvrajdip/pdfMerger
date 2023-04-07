from pypdf import PdfMerger

pdfs = ['cv1.pdf', 'cv2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("cv3.pdf")
merger.close()
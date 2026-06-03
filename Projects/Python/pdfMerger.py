from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

num_of_pdfs = int(input("Enter the number of PDFs to merge: "))

for i in range(0,num_of_pdfs):
    pdf_name = input(f"Enter the name of PDF {i+1} (including .pdf extension): ")
    pdfs.append(pdf_name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()


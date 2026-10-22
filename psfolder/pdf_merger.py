from pypdf import PdfWriter

merger = PdfWriter()
pdf_list = ["1.pdf", "2.pdf", "3.pdf"]

for pdf in pdf_list:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()
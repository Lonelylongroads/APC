from pypdf import PdfWriter

merger = PdfWriter()
pdf_list = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf in pdf_list:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()
#        create new pdf file and add one page or all pages to it from existing pdf

import PyPDF2
# open existing file
file1 = open('LKR.pdf', 'rb')

# read file (binary format)
pdfReader = PyPDF2.PdfReader(file1)


totalPages = len(pdfReader.pages)
print(totalPages)
# choose page to get
page_one = pdfReader.pages[0]


# add page that page to  pdfwriter()(only binary format is supported)
pdfwriter = PyPDF2.PdfWriter()
# pdfwriter.add_page(page_one)


# create new pdf file(use wb instead of rb)
pdf_output = open('new_file7.csv', 'wb')
# now add page to new file from pdfwriter(use write)
# pdfwriter.write(pdf_output)
output = []

for i in range(totalPages):
    page = pdfReader.pages[i]
    pdfwriter.add_page(page)
    # output.append(page)

pdfwriter.write(pdf_output)

# close all opened files
pdf_output.close()
file1.close()


# add all pages to new file
# find total pages


#      for page_num in range(existing_pdf.getNumPages()):
#         page = existing_pdf.getPage(page_num)
#         pdf_writer.addPage(page)

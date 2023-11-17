#               working with pdf using pypdf
# open pdf ,read,extract_text, number of pages..etc

import PyPDF2
file = open('new_file1.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(file)

# count number of pages

totalPages = len(pdfReader.pages)


# print number of pages
print(f"Total Pages: {totalPages}")


# get page

# page_one = pdfReader.pages[0]
 
# covert binary to text format
# page_one_text = page_one.extract_text()

# print(page_one_text)


# extract all pages text
for i in range(totalPages):
    page = pdfReader.pages[i]
    output = page.extract_text()
    print(f"all pages in text format:{output}")




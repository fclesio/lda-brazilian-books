# Thanks Stack Overflow: https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file

# This library should be installed
# $ pip3 install PyPDF2
import PyPDF2

# Filename in project
pdf_book = 'books/pedagogia-oprimido/paulo_freire_pedagogia_do_oprimido.pdf'


# Function to extract all raw text from PDF
def get_text(pdf_file):
    pdf_file_object = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
    count = pdf_reader.numPages
    for i in range(count):
        page = pdf_reader.getPage(i)
        raw_text_unprocessed = page.extractText()
        print(raw_text_unprocessed)


# Just print in screen because the text inside PDF it's
# a mess and a manual cleanup will be necessary to remove the noise
get_text(pdf_book)

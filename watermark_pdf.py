import PyPDF2

template = PyPDF2.PdfFileReader(open('pdf_file_name.pdf', 'rb'))
watermarker_template = PyPDF2.PdfFileReader(open('watermark_pdf_file_name.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPage()):
    page = template.getPage(i)
    page.mergePage(watermarker_template.getPage(0))
    output.addPage(page)

    with open('wartermarker_output.pdf', 'wb') as file:
        output.write(file)


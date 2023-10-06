import PyPDF2

# We want to grab the merged.pdf file as well as the watermark file and combine them.
merged = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# Next we loop through the pages of the merged file and add the watermark to each page
for i in range(merged.getNumPages()):
    page = merged.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_files.pdf', 'wb') as file:
        output.write(file)

from pdfquery import PDFQuery
from lxml import etree

pdf = PDFQuery('sample.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal').text()
print(text_elements)
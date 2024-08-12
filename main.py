import PyPDF2

a= PyPDF2.PdfReader('c.pdf')

str=""
for i in range(1,11):
    str+=a.pages[i].extract_text()

print(str)    
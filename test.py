import PyPDF2

a= PyPDF2.PdfReader('c.pdf')


#print(a.is_encrypted)
print(len(a.pages))

print(a.metadata)
print(a.page_layout)
print(a.pages[2].extract_text())

for i in range(10):
    print(a.pages[i].extract_text())
import PyPDF2
import tkinter as tk
from tkinter import scrolledtext

def pdf_viewer(text):

    window = tk.Tk()
    window.title("Extracted Text")


    text_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
    text_widget.pack(expand=True, fill=tk.BOTH)

    text_widget.insert(tk.END, text)

    #window.resizable(False, False)

    window.mainloop()


a= PyPDF2.PdfReader('c.pdf')

str=""
for i in range(0,len(a.pages)):
    str+=a.pages[i].extract_text()

with open('text.txt','w',encoding='utf-8') as file:
    file.write(str)
          

with open('text.txt', 'r', encoding='utf-8') as file:
    extracted_text = file.read()

pdf_viewer(extracted_text)

import pyttsx3
import tkinter as tk
from tkinter import *

# reading pdffile and extracting text from it using pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def pdfReader(file='AIS_assignment.pdf'):
    # Open the PDF file for reading
    fp = open(file, 'rb')
    # Create a PDF parser using the file pointer
    parser = PDFParser(fp)
    # Create a PDF document using the parser
    doc = PDFDocument(parser)
    # Create a PDF resource manager
    rsrcmgr = PDFResourceManager()
    # Create a string buffer to store the extracted text
    retstr = StringIO()
    # Create a LAParams object
    laparams = LAParams()
    # Create a TextConverter device using the resource manager and string buffer
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF page interpreter using the resource manager and device
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Process each page of the document
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

    # Get the text from the string buffer
    text = retstr.getvalue()
    # Close the file pointer
    fp.close()
    # Close the device
    device.close()
    # Close the string buffer
    retstr.close()
    # Return the extracted text
    return text

def speak(text):
    # initializing the engine
    engine = pyttsx3.init()
    # setting the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # setting the rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 270)
    # setting the volume
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)
    # saying the text
    engine.say(text)
    engine.runAndWait()

def display_text_gui(text):
    root = Tk()
    root.geometry("700x750")
    T = Text(root, height = 100, width = 100)
    l = Label(root, text = "Book of the Day")
    l.config(font =("Courier", 15))
    b1 = Button(root, text = "Next", )
    b2 = Button(root, text = "Exit", command = root.destroy)
    l.pack()
    T.pack()
    b1.pack()
    b2.pack()
    T.insert(tk.END, text)
    tk.mainloop()

def main():
    text = pdfReader()
    display_text_gui(text)
    speak(text)

if __name__ == '__main__':
    main()

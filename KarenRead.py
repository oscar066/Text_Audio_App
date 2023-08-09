from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from colorama import Fore, Back, Style
from io import StringIO
from PIL import Image
import subprocess
import colorama
import pyfiglet
import os

def intro_style_header_text():

    print("\t==============================================")
    print(Fore.BLUE + "\tWelcome to Oscar's Text to Speech Program")
    print("\t==============================================\n")

    def generate_ascii_art(text, font='standard'):
        ascii_art = pyfiglet.figlet_format(text, font=font, justify='center')
        return ascii_art

    name = "OSCAR READS"
    ascii_art = generate_ascii_art(name, font='slant')
    
    colorama.init(autoreset=True)

    print(Fore.CYAN + ascii_art)

def detect_source_format(file):

    print("Please enter the path of the PDF file you would like to read:")
    file = input("Enter the path: ")

    if file[-4:] == '.pdf':
        pdfReader(file=file, output_file='output.txt')
        print(Fore.GREEN + "\n\tPDF Text extracted successfully ")
        text_to_speech(file='output.txt')

    elif file[-4:] == '.png' or file[-4:] == '.jpg':
        print(Fore.GREEN + "\n\tImage Text extracted successfully ")
        tesseractOCR(file=file, output_file='output.txt')
        text_to_speech(file='output.txt')

    elif file[-4:] == '.txt':
        print(Fore.GREEN + "\n\tText File detected")
        text_to_speech(file=file)
        
    else:
        print(Fore.RED + "\tError: File is not a PDF or Image")
        print(Fore.RED + "\tExiting program...")


def pdfReader(file='AIS_assignment.pdf', output_file='output.txt'):
    # Open the PDF file for reading
    fp = open(file, 'rb')
    parser = PDFParser(fp)
    # Create a PDF document using the parser
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    # Create a string buffer to store the extracted text
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()

    # Save the extracted text to the output file
    with open(output_file, 'w', encoding='utf-8') as output_fp:
        output_fp.write(text)

    return output_file

def tesseractOCR(file='E-com_extract.png', output_file='output.txt'):

    image = image.point(lambda x: 0 if x < 135 else 255)
    image.save(newFilePath)

    # call tesseract to do OCR on the newly created image
    subprocess.call(['tesseract',newFilePath,'output'])

    # Open and read the resulting data file
    outputFile = open('output.txt', 'r')
    print(outputFile.read())
    outputFile.close()

    return output_file


def text_to_speech(file=pdfReader()):

    print(Fore.CYAN + "\n\tYour File is ready to be read\n")

    print(Fore.CYAN + "\tPlease select a voice from the following list:")
    print(Fore.CYAN + "\t1. Karen")
    print(Fore.CYAN + "\t2. Alex")
    print(Fore.CYAN + "\t3. Samantha")
    print(Fore.CYAN + "\t4. Victoria")
    print(Fore.CYAN + "\t5. Daniel")

    voice = input(Fore.GREEN + "\nEnter your choice: ")

    voices_map = {
        '1': 'Karen',
        '2': 'Alex',
        '3': 'Samantha',
        '4': 'Victoria',
        '5': 'Daniel'
    }

    if voice in voices_map:
        voice = voices_map[voice]
    else:
        print(Fore.RED + "\tInvalid choice! Defaulting to Karen's voice.")
        voice = 'Karen'

    print(Fore.MAGENTA + "\nChoose a reading speed from 50 to 300 words per minute:")
    speed = input(Fore.GREEN + "Enter your choice: ")

    print(Fore.CYAN  + "\n\tReading your file now...\n")
    os.system(f'say -v {voice} -f {file} -r {speed} --quality=127 -i')

    print(Fore.GREEN + "\nThank you for using Oscar's Text to Speech Program\n")

if __name__ == "__main__":
    intro_style_header_text()
    detect_source_format(file='AIS_assignment.pdf')

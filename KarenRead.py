from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import os
import colorama
from colorama import Fore, Back, Style
import pyfiglet

def pdfReader(file='AIS_assignment.pdf', output_file='output.txt'):
    # Open the PDF file for reading
    
    def generate_ascii_art(text, font='standard'):
        ascii_art = pyfiglet.figlet_format(text, font=font, justify='center')
        return ascii_art

    name = "OSCAR READS"
    ascii_art = generate_ascii_art(name, font='slant')
    
    colorama.init(autoreset=True)

    print(Fore.CYAN + ascii_art)

    print("\t==============================================")
    print(Fore.BLUE + "\tWelcome to Oscar's Text to Speech Program")
    print("\t==============================================\n")

    print("\tPlease enter the path of the PDF file you would like to read:")
    file = input("\tEnter the path: ")

    def is_pdf(file):
        if file[-4:] == '.pdf':
            return True
        else:
            return False

    try:
        if is_pdf(file):
            print(Fore.GREEN + "\n\tText extracted successfully ")
        else:
            raise Exception("\tFile is not a PDF")
    except Exception as e:
        print(Fore.RED + "\tError:", e)
        print(Fore.RED + "\tPlease enter a valid PDF file path")
        print(Fore.RED + "\tExiting program...")

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

def text_to_speech(file=pdfReader()):

    print(Fore.CYAN + "\n\tYour File is ready to be read\n")

    print(Fore.CYAN + "\tPlease select a voice from the following list:")
    print(Fore.CYAN + "\t1. Karen")
    print(Fore.CYAN + "\t2. Alex")
    print(Fore.CYAN + "\t3. Samantha")
    print(Fore.CYAN + "\t4. Victoria")
    print(Fore.CYAN + "\t5. Daniel")

    voice = input(Fore.GREEN + "\tEnter your choice: ")

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

    print(Fore.MAGENTA + "\n\tChoose a reading speed from 50 to 300 words per minute:")
    speed = input(Fore.GREEN + "\tEnter your choice: ")

    print(Fore.CYAN  + "\n\tReading your file now...\n")
    os.system(f'say -v {voice} -f {file} -r {speed} --quality=127 -i')

if __name__ == "__main__":
    text_to_speech()

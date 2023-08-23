from colorama import Fore, Back, Style
import colorama
import pyfiglet
import os
from PdfConverter import *
from ImageConverter import * 
from GuiDisplay import *
from WebTextConverter import *

def detect_source_format(file):

    print("Choose a PDF file you would like to read:")
    # open finder to select a file
    #file = subprocess.run(['open', '-a', 'Finder', file])

    file = input("Enter the path of the file: ")

    if file[-4:] == '.pdf':
        PdfConverter.pdfReader(file=file, output_file='output.txt')
        print(Fore.GREEN + "\n\tPDF Text extracted successfully ")
        text_to_speech(file='output.txt')

    elif file[-4:] == '.png' or file[-4:] == '.jpg':
        print(Fore.GREEN + "\n\tImage Text extracted successfully ")
        ImageConverter.image_to_text(file=file, output_file='output.txt')
        text_to_speech(file='output.txt')

    elif file[-4:] == '.txt':
        print(Fore.GREEN + "\n\tText File detected")
        text_to_speech(file=file)
        
    else:
        print(Fore.RED + "\tError: File is not a PDF or Image")
        print(Fore.RED + "\tExiting program...")


def text_to_speech(file=PdfConverter.pdfReader()):

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
    intro_style = GuiDisplay
    intro_style.intro_style_header_text()
    detect_source_format(file='AIS_assignment.pdf')

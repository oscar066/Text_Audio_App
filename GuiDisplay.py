from colorama import Fore, Back, Style
import colorama
import pyfiglet
import os

class GuiDisplay:
    def __init__(self):
        pass

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
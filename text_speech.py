
import pyttsx3
import PyPDF2

#text = 'Hello World am Mr Creative'
#with open('text.txt', 'r') as f:
    #text = f.read()

def speak(text):
    # initializing the engine
    engine = pyttsx3.init()
    # setting the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # setting the rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    # setting the volume
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)
    # saying the text
    engine.say(text)
    engine.runAndWait()

def pdfReader(file='AIS_assignment.pdf'):
    book = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    for num in range(7, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        return text

def textReader(file='text.txt'):
    with open(file, 'r') as f:
        text = f.read()
    return text

def readWebText(url):
    import requests
    from bs4 import BeautifulSoup
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    text = soup.find('div', class_='entry-content').text
    return text

def main():
    text = pdfReader()
    speak(text)    

if __name__ == '__main__':
    main()



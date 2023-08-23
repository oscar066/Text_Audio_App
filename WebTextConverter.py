import requests
from bs4 import BeautifulSoup

class WebTextConverter:
    def __init__(self, url, web_output):
        self.url = url 
        self.web_output = web_output

    def online_text(self, url, web_output):

        url = input("Enter the URL of the website you would like to read: ")
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        text = soup.get_text()

        with open('online_output.txt', 'w', encoding='utf-8') as output_fp:
            output_fp.write(text)

        return online_output.txt

        
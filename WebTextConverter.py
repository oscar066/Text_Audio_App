import requests
from bs4 import BeautifulSoup

class WebTextConverter:
    def __init__(self, url, web_output):
        self.url = url 
        self.web_output = web_output

    def online_text(url, web_output):
        url = input("Enter the URL of the website you would like to read: ")
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Error: " + str(e))
            return None

        soup = BeautifulSoup(r.content, 'html.parser')
        text = soup.get_text()

        with open(self.web_output, 'w', encoding='utf-8') as output_fp:
            output_fp.write(text)

        return self.web_output


#web = WebTextConverter(url='https://en.wikipedia.org/wiki/The_Communist_Manifesto', web_output='online_web_output.txt')
#output_file = web.online_text()

#if output_file:
   #print(f"Text extracted from website and saved to {output_file}")
#else:
    #print("Error occurred while extracting text from website.")
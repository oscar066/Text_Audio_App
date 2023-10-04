from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

class PdfConverter:
    def __init__(self, file, output_file):
        self.file = file
        self.output_file = output_file

    def pdfReader(file, output_file):
        try:
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

        except FileNotFoundError:
            print("Error: File not found")
            return None

        except Exception as e:
            print("Error: " + str(e))
            return None

from PIL import Image
import subprocess

class ImageConverter:
    def __init__(self, imagefile, imageoutput):
        self.imagefile = imagefile
        self.imageoutput = imageoutput

    def image_to_text(self, imagefile, imageoutput):

        image = image.point(lambda x: 0 if x < 135 else 255)
        image.save(newFilePath)

        # call tesseract to do OCR on the newly created image
        subprocess.call(['tesseract',newFilePath,'output'])

        # Open and read the resulting data file
        outputFile = open('OCR_output.txt', 'r')
        print(outputFile.read())
        outputFile.close()

        return imageoutput


    def text_from_image(self, image):
        pass
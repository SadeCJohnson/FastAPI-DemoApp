import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
import png
from steganography import *
from PIL import Image

#get_pixels_from_image("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")



def retrieve_pixels_from_image():
    image = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")
    
    #resize image for ease
    new_size = (10,10)
    resized_image = image.resize(new_size)
    resized_image.save("newimage.png")
    pixels = list(resized_image.getdata())
    
    print(pixels)
    return pixels



retrieve_pixels_from_image()
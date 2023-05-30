import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
import png
from steganography import *
from PIL import Image
import numpy as np

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

#converts the pixels (with the image data and the encoded message) back into a PNG image
def write_pixels_to_image(pixels, width, height, imageFilename): #TODO: TEST
    image = Image.new('RGB', (width, height))

    image.putdata(pixels)

    image.save(imageFilename)
    #Image.fromarray(np.array(pixels, dtype=np.uint8)) #.save(imageFilename)



#extracts the bytestring from an image
#def decode_pixels(pixels): #TODO: TEST

#retrieves the pixels and bytestring of our original message and combines them
#def enc


def encode_pixels_with_message(pixels, bytestring):
    '''modifies pixels to encode the contents from bytestring'''

    enc_pixels = []
    string_i = 0
    for row in pixels:
        enc_row = []
        for i, char in enumerate(row):
            if string_i >= len(bytestring):
                pixel = row[i]
            else:
                if row[i] % 2 != int(bytestring[string_i]):
                    if row[i] == 0:
                        pixel = 1
                    else:
                        pixel = row[i] - 1
                else:
                    pixel = row[i]
            enc_row.append(pixel)
            string_i += 1

        enc_pixels.append(enc_row)
    return enc_pixels





print("Retrieving pixels from an image: ")
retrieve_pixels_from_image()
print("Encoding pixels with a bytestring message: ")
encode_pixels_with_message(retrieve_pixels_from_image(), "010101010011001001000110011010110101101001010001001111010011110100001010")

#print("Writing pixels to the modified image: ")
#write_pixels_to_image(retrieve_pixels_from_image, 10, 10,  "images/modified-image.png")
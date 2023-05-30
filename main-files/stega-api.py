import asyncio
import base64
from fastapi.responses import FileResponse #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
from fastapi import FastAPI, Query
import png
import json
from stegafuncs import *
from PIL import Image 



program = FastAPI()

#This code is from the exercise found here: https://docs.replit.com/tutorials/python/steganography
@program.get("/encodeMessage") 
def encode_message_as_bytestring(message): #Query param format: ?message="<Insert-String-Here"
    if message.isalpha():
      try:
         b64 = message.encode("utf8")
         bytes_ = base64.encodebytes(b64)
         bytestring = "".join(["{:08b}".format(x) for x in bytes_])
         bytestring += ENDOFMESSAGE
         return bytestring
      except TypeError:
        raise TypeError("Sorry, but this function only takes alphabetic strings as input! Please enter a character between the letters a through z.")
    else:
        raise TypeError("Sorry, but this function only takes alphabetic strings as input! Please enter a character between the letters a through z.")


@program.get("/decodeMessage") #Query param format http://127.0.0.1:8000/decodeMessage?bytestring=<Insert-bytestring-without-quotations>
def decode_message_from_bytestring(bytestring): 
    bytestring = bytestring.split(ENDOFMESSAGE)[0]
    message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
    message = base64.decodebytes(message).decode("utf8")
    return message


@program.get("/displayImage")
def displays_the_original_image():
    return FileResponse("Vibin.png")

@program.get("/retrieveImagePixels")
def retrieve_pixels_from_image():
  pic = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/main-files/Vibin.png")
  pixels = list(pic.getdata())
  return pixels


@program.get("/retrieveImagePixels-async")
async def retrieve_pixels_from_image_async():
    image ="Vibin.png"
    loop = asyncio.get_running_loop()
    image = await loop.run_in_executor(None, Image.open, image)
    pixels = await loop.run_in_executor(None, list, image.getdata())
    return pixels

@program.get("/retrieveResizedImagePixels")
def retrieve_pixels_from_resized_image():
    image = Image.open("Vibin.png")
    new_size = (100,100)
    resized_image = image.resize(new_size)
    resized_image.save("Vibin-resized-img.png")
    pixels = list(resized_image.getdata())
    return pixels #returns the pixels in a list of tuples

#TODO: Need to get these last 2 functions working 
@program.get("/displaySteganographicImage")
def display_Steganographic_Image(bytestring):
   write_pixels_to_image(encode_pixels_with_message(get_pixels_from_image("Vibin-resized-img.png"), bytestring),"Vibin-enc.png")
   return FileResponse("Vibin-enc.png")

@program.get("/decodeSteganographicMessage")
def decode_steganographic_message(): 
   decode_pixels(get_pixels_from_image("Vibin-enc.png")) # need to update this, isn't correct



#Helper functions

def write_pixels_to_image(pixels, fname):
    png.from_array(pixels, 'RGB').save(fname)

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


def get_pixels_from_image(fname):
    pic = Image.open(fname)
    pixels = list(pic.getdata())
    return pixels
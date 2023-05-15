import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
from fastapi import FastAPI, Query
from typing import Annotated #Not sure if this is needed yet... need to do more research
from fastapi.responses import FileResponse
import png
import json
from steganography import *
from PIL import Image 

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"

program = FastAPI()


#TESTING THE INTERACTIVITY OF THE APP - Not yet implemented

#def main():
 #   print(PROMPT)
  #  user_inp = ""
   # while user_inp not in ("1", "2", "q"):
    #    user_inp = input("Your choice: ")

    #if user_inp == "1":
     #   in_image = input("Please enter filename of existing PNG image: ")
       # in_message = input("Please enter the message to encode: ")

        #print("-ENCODING-")
        #pixels = get_pixels_from_image(in_image)
        #epixels = encode_pixels_with_message(pixels, bytestring)
        #write_pixels_to_image(epixels, in_image + "-enc.png")

    #elif user_inp == "2":
     #   in_image = input("Please enter the filename of an existing PNG image: ")
      #  print("-DECODING-")
       # pixels = get_pixels_from_image(in_image)
        #print(decode_pixels(pixels))

#if __name__ == "__main__":
 #   main()

# ---------------------------Actual Code starts below---------------------------------



#This code is from the exercise found here: https://docs.replit.com/tutorials/python/steganography

#TODO: FIX
#Will need to use a Query parameter to pass in value or else a 422 Unprocessable Entity error will be returned
@program.get("/encodeMessage") 
def encode_message_as_bytestring(message): #Query param format: ?message="<Insert-String-Here"
    if message.isalpha():
      try:
         b64 = message.encode("utf8") #Unicode Transformation Format - 8 bits (UTF-8) encodes the characters as ASCII text aka in human readable / natural form
         bytes_ = base64.encodebytes(b64) #encodes the message using base64 encoded data into the binary form
         bytestring = "".join(["{:08b}".format(x) for x in bytes_]) #Tranformation of the binary form into a sequence of bytes (which allows the data to be stored in a computer)
         return bytestring

      except TypeError:
        return "Sorry, but this function only takes alphabetic strings as input! Please enter a character between the letters a through z."
    else:
        return "Sorry, but this function only takes alphabetic strings as input! Please enter a character between the letters a through z."


@program.get("/decodeMessage") #Query param format http://127.0.0.1:8000/decodeMessage?bytestring=<Insert-bytestring-without-quotations>
def decode_message_from_bytestring(bytestring): 
    bytestring = bytestring.split(ENDOFMESSAGE)[0]
    message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
    message = base64.decodebytes(message).decode("utf8")
    return message

#returns a provided image that'll serve as the use case for this steganography project
#Source: https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
@program.get("/displayImage")
def displays_the_original_image():
    return FileResponse("images/scj-avatar.png")


@program.get("/retrieveImagePixels")
def retrieve_pixels_from_image():
    #image = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")
    #pixels = list(image.getdata())
    #return pixels

    image = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")
    
    #resize image for ease
    new_size = (100,100)
    resized_image = image.resize(new_size)
    resized_image.save("newimage.png")
    pixels = list(resized_image.getdata())
    
    print(pixels)
    return pixels

@program.get("/displayResizedImage")
def retrieve_resized_image():
    image = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")
    
    #resize image for ease
    new_size = (100,100)
    resized_image = image.resize(new_size)
    resized_image.save("images/scj-avatar-resized.png")
    #pixels = list(resized_image.getdata())
    
    #print(pixels)
    return FileResponse("images/scj-avatar-resized.png")

@program.get("/displaySteganographicImage")
def display_Steganographic_Image(bytestring):
   image = Image.open("/Users/sjohnson/Desktop/techie-projects/FastAPI-DemoApp/program-files/images/scj-avatar.png")
    
    #resize image for ease
   resized_image = image.resize((100,100))
   resized_image.save("scj-unencoded-pic.png")
   pixels = list(resized_image.getdata())
    
   write_pixels_to_image(encode_pixels_with_message(pixels, bytestring),"scj-encoded-pic.png")
   
   return FileResponse("scj-encoded-pic.png")

   #write_pixels_to_image(encode_message_as_bytestring(pixels,bytestring), scj-encoded.png) 


    #return "Endpoint Under Construction - COMING SOON"


#@program.get("/decodeSteganographicMessage")
#def decode_steganographic_message(): TODO

#This function was created for naming convention testing purposes
#@program.get("/displaySteganographicImage-2")
#def displaySteganographicImage():
#    return "Improper format"
# ***************INPUT 1******************
# http://127.0.0.1:8000/encodeMessage?message=%22Sade%22

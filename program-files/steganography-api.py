import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
from fastapi import FastAPI
from fastapi.responses import FileResponse
import png
import json
from PIL import Image 

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"

program = FastAPI()

#This code is from the exercise found here: https://docs.replit.com/tutorials/python/steganography

#Will need to use a Query parameter to pass in value or else a 422 Unprocessable Entity error will be returned
@program.get("/encodeMessage") 
def encode_message_as_bytestring(message): #Query param format: ?message="<Insert-String-Here"
    b64 = message.encode("utf8") #Unicode Transformation Format - 8 bits (UTF-8) encodes the characters as ASCII text aka in human readable / natural form
    bytes_ = base64.encodebytes(b64) #encodes the message using base64 encoded data into the binary form
    bytestring = "".join(["{:08b}".format(x) for x in bytes_]) #Tranformation of the binary form into a sequence of bytes (which allows the data to be stored in a computer)
    return bytestring

@program.get("/decodeMessage") #Query param format http://127.0.0.1:8000/decodeMessage?bytestring=<Insert-bytestring-without-quotations>
def decode_message_from_bytestring(bytestring): 
    bytestring = bytestring.split(ENDOFMESSAGE)[0]
    message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
    message = base64.decodebytes(message).decode("utf8")
    return message

#returns a provided image that'll serve as the use case for this steganography project
#Source: https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
@program.get("/displayImage")
def displayImage():
    return FileResponse("images/scj-avatar.png")


@program.get("/imagePixels")
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

# ***************INPUT 1******************
# http://127.0.0.1:8000/encodeMessage?message=%22Sade%22


#  ***************OUTPUT 1****************
# "010010010110110001001110011010000101101001000111010101010110100100001010"
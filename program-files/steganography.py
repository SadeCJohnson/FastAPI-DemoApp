import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
import png

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"

#This code is from the exercise found here: https://docs.replit.com/tutorials/python/steganography
#Encodes a specified message into a bytestring
def encode_message_as_bytestring(message): #TESTED
    b64 = message.encode("utf8") #Unicode Transformation Format - 8 bits (UTF-8) encodes the characters as ASCII text aka in human readable / natural form
    print(b64) #this prints the human readable message that was passed in the exact form that it was passed in as a parameter
    bytes_ = base64.encodebytes(b64) #encodes the message using base64 encoded data into the binary form
    print(bytes_) #prints the transformation into binary form
    bytestring = "".join(["{:08b}".format(x) for x in bytes_]) #Tranformation of the binary form into a sequence of bytes (which allows the data to be stored in a computer)
    print(bytestring)
    return bytestring


#retrieves pixels from an image
def get_pixels_from_image(imageFilename): #deprecated this function
    image = png.Reader(imageFilename).read() #The read() method returns a 4-tuple consisting of the width, height, rows (pixels), and additional metadata
    pixels = image[2]
    print("The width of the image is: " )
    print(image[0])
    print("The height of the image is: " )
    print(image[1])
    print("The rows (pixels) of the image are: " )
    print(image[2])
    print("Additional Metadata of the image is: " )
    print(image[3])
   # print(type(image))
    return pixels


#retrieves the pixels and bytestring of our original message and combines them
def encode_pixels_with_message(pixels, bytestring): #TODO: TEST
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

#converts the pixels (with the image data and the encoded message) back into a PNG image
def write_pixels_to_image(pixels, imageFilename): #TODO: TEST
    png.from_array(pixels, 'RGB').save(imageFilename)

#converts a binary string back into human readable text
def decode_message_from_bytestring(bytestring): #TESTED
    bytestring = bytestring.split(ENDOFMESSAGE)[0]
    message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
    message = base64.decodebytes(message).decode("utf8")
    return message

#extracts the bytestring from an image
def decode_pixels(pixels): #TODO: TEST
    bytestring = []
    for row in pixels:
        for c in row:
            bytestring.append(str(c % 2))
    bytestring = ''.join(bytestring)
    message = decode_message_from_bytestring(bytestring)
    return message



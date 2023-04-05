import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)
import png
from steganography import *


#TEST 1: THE ENCODE FUNCTION
print("Testing the function that returns the metadata of an image:\n ")
encode_message_as_bytestring("Sade")
encode_message_as_bytestring("sade")
print("____________________________________________________________")

#TEST 2: PIXEL RETRIEVAL FROM AN IMAGE amongst other information
print("Testing the function that returns the metadata of an image:\n ")
get_pixels_from_image("scj-avatar.png")
print("____________________________________________________________")

#TEST 3: Tests the Decode function to see that the bytestring is returning the correct human readable string
print("Testing the function that decodes a given bytestring into human readable text:\n ")
decoder1 = decode_message_from_bytestring("010101010011001001000110011010110101101001010001001111010011110100001010")
print(decoder1)
print(decode_message_from_bytestring("011000110011001001000110011010110101101001010001001111010011110100001010"))


 

#  ***************OUTPUT FOR TEST 1****************
#The first test for the encode_message_as_bytestring(...) function returns the following output:
#b'Sade'
#b'U2FkZQ==\n'
#010101010011001001000110011010110101101001010001001111010011110100001010

#The second test for the encode_message_as_bytestring(...) function returns a slightly different output:
#b'sade'
#b'c2FkZQ==\n'
#011000110011001001000110011010110101101001010001001111010011110100001010

#  ***************OUTPUT FOR TEST 2****************
#The test of the get_pixels_from_image(...) function returns the following output
#The width of the image is: 
#368
#The height of the image is: 
#357
#The rows (pixels) of the image are: 
#<generator object Reader._iter_bytes_to_values at 0x10b16c580>
#Additional Metadata of the image is: 
#{'greyscale': False, 'alpha': True, 'planes': 4, 'bitdepth': 8, 'interlace': 0, 'size': (368, 357)}


#  ***************OUTPUT FOR TEST 3****************
# The test for the decode_message_from_bytestring(...) functions returns the following:
# Testing the function that decodes a given bytestring into human readable text:
# Sade
# sade


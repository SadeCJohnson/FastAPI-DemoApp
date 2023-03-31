import base64 #base64 uses 64 possible values for representing binary data (https://levelup.gitconnected.com/an-introduction-to-base64-encoding-716cdccc58ce)

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"

#This code is from the exercise found here: https://docs.replit.com/tutorials/python/steganography

def encode_message_as_bytestring(message):
    b64 = message.encode("utf8") #Unicode Transformation Format - 8 bits (UTF-8) encodes the characters as ASCII text aka in human readable / natural form
    print(b64) #this prints the human readable message that was passed in the exact form that it was passed in as a parameter
    bytes_ = base64.encodebytes(b64) #encodes the message using base64 encoded data into the binary form
    print(bytes_) #prints the transformation into binary form
    bytestring = "".join(["{:08b}".format(x) for x in bytes_]) #Tranformation of the binary form into a sequence of bytes (which allows the data to be stored in a computer)
    print(bytestring)
    return bytestring


encode_message_as_bytestring("Sade")
encode_message_as_bytestring("sade")




#  ***************OUTPUT****************
#Line 17 returns the following output
#b'Sade'
#b'U2FkZQ==\n'
#010101010011001001000110011010110101101001010001001111010011110100001010

#Line 18 returns a slightly different output:
#b'sade'
#b'c2FkZQ==\n'
#011000110011001001000110011010110101101001010001001111010011110100001010


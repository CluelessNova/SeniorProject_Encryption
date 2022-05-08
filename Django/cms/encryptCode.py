from email.mime import base
import random, base64


def printHello(num):

    print("Hello World")
    return (num + "Successfully executed the python file")

def key(secure):
    key = []
    i = 0
    num = int(secure)
    while i < num:
        x = random.randint(1,25)
        key.append(str(x)+ ' ')
        i+=1
    print("Hello World")
    return key
    # return (secure + "Successfully executed the python file")


def encryptMess(key, message):
    encrypted = ""
    i = 0
    
    keyInput = key.split(' ')
    shiftKey = list(map(int, keyInput))
    # print(shiftKey)
    # print(message)

    for char in message:
        if char.isupper(): #check if it's an uppercase character
            if i >= len(shiftKey):
                i = 0
            char_index = ord(char) - ord('A')
            # shift the current character by key positions
            char_shifted = (char_index + shiftKey[i]) % 26 + ord('A')
            char_new = chr(char_shifted)
            encrypted += char_new
            i += 1
        elif char.islower(): #check if its a lowecase character
            if i >= len(shiftKey):
                i = 0
            # subtract the unicode of 'a' to get index in [0-25) range
            char_index = ord(char) - ord('a') 
            char_shifted = (char_index + shiftKey[i]) % 26 + ord('a')
            char_new = chr(char_shifted)
            encrypted += char_new
            i += 1
        elif char.isdigit():
            if i >= len(shiftKey):
                i = 0
            # if it's a number,shift its actual value 
            char_new = (int(char) + shiftKey[i]) % 10
            encrypted += str(char_new)
            i += 1
        else:
            # if its neither alphabetical nor a number, just leave it like that
            encrypted += char
    messageBytes = encrypted.encode('ascii')
    base64Bytes= base64.b64encode(messageBytes)
    encrytpedMessage = base64Bytes.decode('ascii')
    return encrytpedMessage
    

def decryptMess(key, encMess):
    decrypted = ""
    # print(key)
    # print(encMess)

    base64Bytes = encMess.encode('ascii')
    messageBytes = base64.b64decode(base64Bytes)
    message = messageBytes.decode('ascii')
    keyInput = key.split(' ')
    shiftKey = list(map(int, keyInput))
    i = 0

    for char in message:
        if char.isupper(): 
            if i >= len(shiftKey):
               i = 0
            char_index = ord(char) - ord('A')
            # shift the current character to left by key positions to get its original position
            char_og_pos = (char_index - shiftKey[i]) % 26 + ord('A')
            char_og = chr(char_og_pos)
            decrypted += char_og
            i += 1
                    
        elif char.islower(): 
            if i >= len(shiftKey):
                i = 0
            char_index = ord(char) - ord('a') 
            char_og_pos = (char_index - shiftKey[i]) % 26 + ord('a')
            char_og = chr(char_og_pos)
            decrypted += char_og
            i += 1
                    
        elif char.isdigit():
            if i >= len(shiftKey):
                i = 0
            # if it's a number,shift its actual value 
            char_og = (int(char) - shiftKey[i]) % 10
            decrypted += str(char_og)
            i += 1
                    
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += char

    return decrypted
import random 

class encryption:

    def __init__(self):
        self.key = []
        self.secureness = 0
        self.encryptMessage = ""

    #create a key that will be used for the ecnryption
    def generateKey(self, secureness):
        self.secureness = secureness
        i = 0
        while i < self.secureness:
            x = random.randint(1,25)

            self.key.append(x)
            i += 1
        # print("Your key has been generated!")
        return self.key
       

    def displayKey(self):
        return self.key
        

    #encrypt the message
    def encrypt(self, message, key):
        encrypted = ""
        i = 0
        shiftKey = key

        for char in message:
                if char.isupper(): #check if it's an uppercase character
                    if i >= len(key):
                        i = 0
                    char_index = ord(char) - ord('A')
                    # shift the current character by key positions
                    char_shifted = (char_index + shiftKey[i]) % 26 + ord('A')
                    char_new = chr(char_shifted)
                    encrypted += char_new
                    i += 1
                elif char.islower(): #check if its a lowecase character
                    if i >= len(key):
                        i = 0
                    # subtract the unicode of 'a' to get index in [0-25) range
                    char_index = ord(char) - ord('a') 
                    char_shifted = (char_index + shiftKey[i]) % 26 + ord('a')
                    char_new = chr(char_shifted)
                    encrypted += char_new
                    i += 1
                elif char.isdigit():
                    if i >= len(key):
                        i = 0
                    # if it's a number,shift its actual value 
                    char_new = (int(char) + shiftKey[i]) % 10
                    encrypted += str(char_new)
                    i += 1
                else:
                    # if its neither alphabetical nor a number, just leave it like that
                    encrypted += char

        self.encryptMessage = encrypted
        return encrypted

    def displayMessage(self):
        return self.encryptMessage


class decryption:

    def __init__(self):
        self.key = []
        self.decryptMessage = ""

    
    #take in key from sender
    def keyImport(self):
        #checks if key is correct 

        #if key is correct, run decrypt

        #if not, throw exception
        pass

    def decrypt(self, encMessage, key):
        decrypted = ""
        shiftKey = key
        i = 0

        for char in encMessage:
                if char.isupper(): 
                    if i >= len(key):
                        i = 0
                    char_index = ord(char) - ord('A')
                    # shift the current character to left by key positions to get its original position
                    char_og_pos = (char_index - shiftKey[i]) % 26 + ord('A')
                    char_og = chr(char_og_pos)
                    decrypted += char_og
                    i += 1
                    
                elif char.islower(): 
                    if i >= len(key):
                        i = 0
                    char_index = ord(char) - ord('a') 
                    char_og_pos = (char_index - shiftKey[i]) % 26 + ord('a')
                    char_og = chr(char_og_pos)
                    decrypted += char_og
                    i += 1
                    
                elif char.isdigit():
                    if i >= len(key):
                        i = 0
                    # if it's a number,shift its actual value 
                    char_og = (int(char) - shiftKey[i]) % 10
                    decrypted += str(char_og)
                    i += 1
                    
                else:
                    # if its neither alphabetical nor a number, just leave it like that
                    decrypted += char

        self.decryptMessage = decrypted
        return decrypted

    def displayMessage(self):
        return self.decryptMessage


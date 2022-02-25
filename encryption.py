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
            x = random.randint(0,9)

            self.key.append(x)
            i += 1
        print("Your key has been generated!")
       

    #Test to see if adding to the 'key' was working
    # def manAdd(self, num):
    #     self.key.append(num)

    def displayKey(self):
        # print("Your key is:") 
        # print(self.key)
        return self.key
        

    #encrypt the message
    def encrypt(self, message, shiftKey):
        encrypted = ""

        for char in message:

            if char.isupper(): #check if it's an uppercase character
                char_index = ord(char) - ord('A')
                # shift the current character by key positions
                char_shifted = (char_index + shiftKey) % 26 + ord('A')
                char_new = chr(char_shifted)
                encrypted += char_new
            elif char.islower(): #check if its a lowecase character
                # subtract the unicode of 'a' to get index in [0-25) range
                char_index = ord(char) - ord('a') 
                char_shifted = (char_index + shiftKey) % 26 + ord('a')
                char_new = chr(char_shifted)
                encrypted += char_new
            elif char.isdigit():
                # if it's a number,shift its actual value 
                char_new = (int(char) + shiftKey) % 10
                encrypted += str(char_new)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                encrypted += char

        self.encryptMessage = encrypted
        return encrypted

    def displayMessage(self):
        return self.encryptMessage


class decyption:

    def __init__(self):
        self.key = []
        self.decryptMessage = ""

    
    #take in key from sender
    def keyImport(self):
        #checks if key is correct 

        #if key is correct, run decrypt

        #if not, throw exception
        pass

    def decrypt(self, encMessage, shiftKey):
        decrypted = ""

        for char in encMessage:
            if char.isupper(): 
                char_index = ord(char) - ord('A')
                # shift the current character to left by key positions to get its original position
                char_og_pos = (char_index - shiftKey) % 26 + ord('A')
                char_og = chr(char_og_pos)
                decrypted += char_og
            elif char.islower(): 
                char_index = ord(char) - ord('a') 
                char_og_pos = (char_index - shiftKey) % 26 + ord('a')
                char_og = chr(char_og_pos)
                decrypted += char_og
            elif char.isdigit():
                # if it's a number,shift its actual value 
                char_og = (int(char) - shiftKey) % 10
                decrypted += str(char_og)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                decrypted += char

        self.decryptMessage = decrypted
        return decrypted

    def displayMessage(self):
        return self.decryptMessage

# from curses import keyname
import random 

# secureness = input("How secure of a key do you want? (state in numbers)")

# key = []
# i = 0

# while i < secureness:
#     x = random.randint(0, 9)

#     key.append(x)
#     i += 1


# print(key)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class encrypt:
#     def __init__(self, securness):
#         self.key = []
#         self.secureness = securness

#     def generateKey(self):
#         i = 0
#         while i < self.secureness:
#             x = random.randint(0,9)

#             self.key.append(x)
#             i += 1

#     def manAdd(self, num):
#         self.key.append(num)

#     def displayKey(self):
#         print(self.key)


# test = encrypt(10)
# test.displayKey()
# test.generateKey()
# test.displayKey()
# test.manAdd(10)
# test.displayKey()


# def encrypt(text,s):
#     result = ""
 
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
 
#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
 
#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
 
#     return result

# text = "ATTACKATONCE"
# s = 4
# print ("Text  : " + text)
# print ("Shift : " + str(s))
# print ("Cipher: " + encrypt(text,s))
# print ("Cipher: " + encrypt("Hello World",s))
# print ("Cipher: " + encrypt("HelloWorld",s))


# The Encryption Function
def cipher_encrypt(plain_text, key):
    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character
            c_index = ord(c) - ord('A')
            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #check if its a lowecase character
            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):
    decrypted = ""

    for c in ciphertext:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"
ciphertext = cipher_encrypt(plain_text, 2)
print("Plain text message:\n", plain_text)
print("Encrypted ciphertext:\n", ciphertext)
print(" ")
ciphertext = "Qexi, xli ehzirxyvi vmhi mr Gerfivve aew ws qygl jyr, Ai aivi ws hvyro ai irhih yt geppmrk 355!"
decrypted_msg = cipher_decrypt(ciphertext, 4)
print("The cipher text:\n", ciphertext)
print("The decrypted message is:\n",decrypted_msg)
print(" ")
ciphertext = "Sr xli gsyrx sj 7, 6, 5 - Ezirkivw Ewwiqfpi!"
decrypted_msg = cipher_decrypt(ciphertext, 4)
print("The cipher text:\n", ciphertext)
print("The decrypted message is:\n",decrypted_msg)

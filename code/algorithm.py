import string
from encryption import decryption, encryption 
e = encryption()
d = decryption()

user_message = input("What is your message? ")
user_secure = input("How secure would you like the key be? ")

e.generateKey(user_secure)
e.encrypt("user_message", e.key)

print(e.displayMessage())

user_input_key = input("Would you like to see the key? ")
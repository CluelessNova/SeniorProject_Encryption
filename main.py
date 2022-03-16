from encryption import encryption
from encryption import decryption

encrypt = encryption()
decrypt = decryption()
random = encryption()

encrypt.generateKey(4)
print(encrypt.displayKey())
encrypt.encrypt("Hello World", encrypt.key)
print("They encrpyted message is: ")
print(encrypt.displayMessage())
print(" ")
decrypt.decrypt(encrypt.encryptMessage, encrypt.key)
print("The decrypted message is: ")
print(decrypt.displayMessage())
print(" ")

random.generateKey(4)
print("Someone else trying to get message: ")
print(random.displayKey())
decrypt.decrypt(encrypt.encryptMessage, random.key)
print(decrypt.displayMessage())

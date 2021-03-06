from encryption import encryption
from encryption import decryption

encrypt = encryption()
decrypt = decryption()
random = encryption()

encrypt.generateKey(15)
print(encrypt.displayKey())
encrypt.encrypt("This is my test message. If you can see this, you have the correct key", encrypt.key)
print("They encrypted message is: ")
print(encrypt.displayMessage())
print(" ")
decrypt.decrypt(encrypt.encryptMessage, encrypt.key)
print("The decrypted message is: ")
print(decrypt.displayMessage())
print(" ")

random.generateKey(5)
print("Someone else trying to get message: ")
print(random.displayKey())
decrypt.decrypt(encrypt.encryptMessage, random.key)
print(decrypt.displayMessage())

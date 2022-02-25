from encryption import encryption
from encryption import decyption

encrypt = encryption()
decrypt = decyption()

encrypt.generateKey(10)
print(encrypt.displayKey())
print(encrypt.displayKey())
encrypt.encrypt("Hello World", 4)
print(encrypt.displayMessage())

decrypt.decrypt("Lipps Asvph", 4)
print(decrypt.displayMessage())

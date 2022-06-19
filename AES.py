# Buch S.55

from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

from cryptography.hazmat.backends import default_backend
import os

input = b"A1234567890123456B" # ''Unicode, b' Bytes Deklaration

key = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key),
                   modes.ECB(),
                   backend=default_backend() )

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

encrypted= aesEncryptor.update(input)

print( encrypted )

print( aesDecryptor.update(encrypted))
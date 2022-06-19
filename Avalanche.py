#Avalanche Effekt Testen, Practical Cryptography in Python Page 34

import hashlib

hexstring = hashlib.md5(b'bob').hexdigest()
print(hexstring)
binstring = bin(int(hexstring, 16))
print("{}\n{}".format(binstring[2:66], binstring[66:]))

# Veränderung von Bob auf Cob Ändert 64 von 128 bits
hexstring = hashlib.md5(b'Cob').hexdigest()
print(hexstring)
binstring = bin(int(hexstring, 16))
print("{}\n{}".format(binstring[2:66], binstring[66:]))

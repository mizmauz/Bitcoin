# XOR Python

# 5 XOR 9 = 12

#     0011 5
# XOR 1001 9
#     1010 12

#     1000 8
# XOR 0001 1
#     1001 9

#     1000 8
# OR  0001 1
#     1001 1

#     1000 8
# AND 0001 1
#     0000 0

input = 8

print(bin(input))

print(int('f', 16)) #"Nummer in Integer konvertieren, Basis = 16"
print(int('1000', 2)) #"Nummer in Integer konvertieren, Basis = 2"

output_xor = input ^ 1
output_and = input & 1
output_or  = input | 1

print( output_xor )
print( output_and )
print( output_or )
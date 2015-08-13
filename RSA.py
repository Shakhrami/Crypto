#?/usr/beqin/env python

#Simple RSA version 1
#Only works for one letter messages; want to make it work for a string.
def find_d(e, phi):
    for i in range(1, phi):
        if((e*i)%phi == 1):
            return i

def encrypt(message,e,p,q):
    letterToNum = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7,
                   "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14,
                   "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21,
                   "W":22, "X":23, "Y":24, "Z":25, " ":26}

    cipherText = []
    for char in message:
        cipherText.append((letterToNum[char]**e)%(p * q))
    
    return cipherText
    
def decrypt(cipherText,d,p,q):
    plainText = []
    for num in cipherText:
        plainText.append((num**d)%(p * q))
    
    return plainText

def translate(plainText):
    numToLetter = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H",
                   8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O",
                   15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V",
                   22:"W", 23:"X", 24:"Y", 25:"Z", 26:" "}
    message = ""
    for num in plainText:
        message += numToLetter[num]
    return message

p = 3   #prime 1. These should be large primes
q = 11  #prime 2
phi = (p-1)*(q-1)

e = 3  # public key. Note: gcd(e, phi) = 1
d = find_d(e, phi) # private key

secretMessage = "E"
cipher = encrypt(secretMessage,e,p,q)
print cipher
plainText = decrypt(cipher,d,p,q)
print plainText
print translate(plainText)
    
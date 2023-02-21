# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            # if letter is uppercase and in second half of the alphabet
            if ord(char) > 77 and ord(char)<= 90:
                h = 65 + 13 - (91 - ord(char))
                result += chr(h)
            # if letter is lowercase and in second half of the alphabet
            elif ord(char) > 109 and ord(char)<= 122:
                k = 97 + 13 - (123 - ord(char))
                result += chr(k)
            else:
                l = ord(char) + 13
                result += chr(l)
        else: 
            result += char
    return result

# top solution
import string

def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
    return outputMessage
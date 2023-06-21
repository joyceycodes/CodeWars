# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

def decrypt(encrypted_text, n):
    result = encrypted_text
    
    while n > 0:
        evens = result[len(result)//2:]
        odds = result[:len(result)//2]
        text = ""
        for i in range(len(result)//2):
            text += evens[i]
            text += odds[i]
            
        if len(result)% 2 == 1:
            text += evens[-1]
        result = text
        n -= 1

    return result


def encrypt(text, n):
    result = text
    while n > 0:
        evens = ''
        odds = ''
        for i in range(len(result)):
            if i % 2 == 1:
                odds += result[i]
            else:
                evens += result[i]
        result = odds + evens
        n-=1

    return result

# top solution
def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
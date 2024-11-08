plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    text = plain_text.lower()
    result = ""
    count = 0

    for i in text:
        if i in plain:
            if count == 5:
                result += " "
                count = 0
            result += cipher[plain.index(i)]
            count += 1
            
        if i.isdigit():
            if count == 5:
                result += " "
                count = 0
            result += i
            count += 1
            
    return result


def decode(ciphered_text):
    result = ""

    for i in ciphered_text:
        if i in cipher:
            result += plain[cipher.index(i)]
            
        if i.isdigit():
            result += i
            
    return result

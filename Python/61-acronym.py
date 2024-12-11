import string

def abbreviate(words):
    word_list = words.replace("-", " ").translate(str.maketrans("", "",string.punctuation)).split()
    result = ""

    for word in word_list:
        result += word[0].upper()
            
    return result

def is_isogram(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("-", "")

    for letter in string:
        if string.count(letter) > 1:
            return False

    return True

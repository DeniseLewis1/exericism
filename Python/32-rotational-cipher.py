def rotate(text, key):
    result = ""

    for letter in text:
        new_ord = 0

        if letter >= "a" and letter <= "z":
            new_ord += ord(letter) + key
            if new_ord > ord("z"):
                new_ord -= 26
        elif letter >= "A" and letter <= "Z":
            new_ord += ord(letter) + key
            if new_ord > ord("Z"):
                new_ord -= 26
        else:
            new_ord += ord(letter)

        result += chr(new_ord)

    return result

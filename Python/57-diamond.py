def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    index = alphabet.index(letter)
    width = 2 * index + 1
    diamond = []

    for i in range(index + 1):
        row = [" "] * width
        row[index - i] = alphabet[i]
        row[index + i] = alphabet[i]
        diamond.append("".join(row))

    for i in range(index - 1, -1, -1):
        diamond.append(diamond[i])
        
    return diamond

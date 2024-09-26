def to_rna(dna_strand):
    result = ""

    for letter in dna_strand:
        if letter == "G":
            result += "C"
        elif letter == "C":
            result += "G"
        elif letter == "T":
            result += "A"
        elif letter == "A":
            result += "U"
        else:
            result += letter

    return result

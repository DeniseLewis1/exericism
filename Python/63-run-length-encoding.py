def decode(string):
    result = ""
    count = ""
    
    for char in string:
        print(char, count, result)
        if char.isnumeric():
            count += char
        else:
            if count:
                result += char * int(count)
                count = ""
            else:
                result += char
    return result


def encode(string):
    result = ""
    count = 1

    if string == "":
        return ""

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            if count > 1:
                result += str(count)
                count = 1

            result += string[i-1]

    if count > 1:
            result += str(count)

    result += string[len(string)-1]
 
    return result

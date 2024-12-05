def say(number):
    numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    result = ""

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    if number in numbers:
        return numbers[number]
    
    if number < 100:
        return f"{numbers[number // 10 * 10]}-{numbers[number % 10]}"

    if number < 1000:
        if number % 100 == 0:
            return f"{numbers[number // 100]} hundred"
        else:
            return f"{numbers[number // 100]} hundred {say(number % 100)}"

    if number < 1000000:
        if number % 1000 == 0:
            return f"{say(number // 1000)} thousand"
        else:
            return f"{say(number // 1000)} thousand {say(number % 1000)}"

    if number < 1000000000:
        if number % 1000000 == 0:
            return f"{say(number // 1000000)} million"
        else:
            return f"{say(number // 1000000)} million {say(number % 1000000)}"

    if number % 1000000000 == 0:
        return f"{say(number // 1000000000)} billion"
    else:
        return f"{say(number // 1000000000)} billion {say(number % 1000000000)}"
            

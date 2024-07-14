def is_armstrong_number(number):
    num_list = list(str(number))
    total = 0
    
    for num in num_list:
        total += int(num) ** len(num_list)

    return number == total

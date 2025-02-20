def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    num_to_check = 1
    count = 0

    while count < number:
        num_to_check += 1
        
        if is_prime(num_to_check):
            count += 1
            
    return num_to_check

def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10 or (not isbn[-1].isnumeric() and isbn[-1] != 'X') or (isbn[-1] == 'X' and not isbn[:-2].isnumeric()) or not isbn[:-1].isnumeric():
        return False

    num_isbn = list(isbn)  
    if num_isbn[-1] == 'X':
        num_isbn[-1] = 10

    num_isbn = [int(digit) for digit in num_isbn]

    return (num_isbn[0] * 10 + num_isbn[1] * 9 + num_isbn[2] * 8 + num_isbn[3] * 7 + num_isbn[4] * 6 + num_isbn[5] * 5 + num_isbn[6] * 4 + num_isbn[7] * 3 + num_isbn[8] * 2 + num_isbn[9] * 1) % 11 == 0
    
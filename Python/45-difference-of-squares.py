def square_of_sum(number):
    return (sum(i for i in range(1, number + 1))) ** 2


def sum_of_squares(number):
    return sum(i ** 2 for i in range(1, number + 1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

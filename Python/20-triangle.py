def equilateral(sides):
    a, b, c = sides
    return is_trianlge(sides) and (a == b and b == c)


def isosceles(sides):
    a, b, c = sides
    return is_trianlge(sides) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return is_trianlge(sides) and (a != b and a != c and b != c)


def is_trianlge(sides):
    a, b, c = sides
    return min(sides) > 0 and a + b >= c and b + c >= a and a + c >= b
def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []

    for i in lists:
        result += i

    return result

def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    len = 0

    for i in list:
        len += 1
    
    return len


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    total = initial

    for i in list:
        total = function(total, i)

    return total


def foldr(function, list, initial):
    total = initial

    for i in list[::-1]:
        total = function(total, i)

    return total


def reverse(list):
    return list[::-1]

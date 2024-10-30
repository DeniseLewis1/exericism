def sum_of_multiples(limit, multiples):
    set = []

    for multiple in multiples:
        for i in range(limit):
            if multiple > 0 and i % multiple == 0 and i not in set:
                set.append(i)

    return sum(set)

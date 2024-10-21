def flatten(iterable):
    flat_list = []

    for item in iterable:
        if type(item) != list and item is not None:
            flat_list.append(item)
            
        if type(item) == list:
            flat_list += flatten(item)

    return flat_list

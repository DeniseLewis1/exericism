def find(search_list, value):
    start = 0
    end = len(search_list) - 1
    mid = 0

    while start <= end:
        mid = (start + end) // 2

        if value < search_list[mid]:
            end = mid - 1
        elif value > search_list[mid]:
            start = mid + 1
        else:
            return mid
    
    raise ValueError("value not in array")

def binary_search(list, suchwert, i_min, i_max) -> int:
    '''
    Binary search returns the index of the wanted value, or -1 if not found.
    '''
    if i_min > i_max:
        return -1
    i_middle = (i_min + i_max) // 2
    if list[i_middle] == suchwert:
        return i_middle
    elif list[i_middle] > suchwert:
        return binary_search(list, suchwert, i_min, i_middle - 1)
    else:
        return binary_search(list, suchwert, i_middle + 1, i_max)


# zahlen = list(range(100000000))
zahlen = [12, 33, 56, 79, 81, 82, 83, 99]
idx = binary_search(zahlen, 83, 0, len(zahlen) - 1)
print(idx)

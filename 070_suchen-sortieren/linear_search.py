zahlen = list(range(100000000))


def linear_search(list, suchwert, i_min, i_max) -> int:
    for n in range(i_min, i_max):
        if list[n] == suchwert:
            return n
    return -1



idx = linear_search(zahlen, 590540, 0, len(zahlen) - 1)
print(idx)
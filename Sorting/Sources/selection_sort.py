def selection_sort(list):
    length = len(list)
    for i in range(length):
        minimum = i
        for j in range(i+1, length):
            if list[j] < list[minimum]:
                minimum = j
        list[i], list[minimum] = list[minimum], list[i]
    return list

def bubble_sort(list):
    changed = True
    while changed:
        changed = False
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                changed = True
    return list

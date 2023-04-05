def quick_sort(list):
    length = len(list)
    if(length > 1):
        left = []
        middle = []
        right = []
        for i in list:
            if(i > list[0]):
                right.append(i)
            elif(i == list[0]):
                middle.append(i)
            else:
                left.append(i)
        return quick_sort(left) + middle + quick_sort(right)
    else:
        return list

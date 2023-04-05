def prefix_table(pattern):
    table = []
    for i in range(len(pattern)):
        table.append(0)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[length] == pattern[i]:
            length += 1
            table[i] = length
            i += 1
        elif length > 0:
            length = table[length - 1]
        else:
            i += 1
    return table


def find(pattern, text):
    p = len(pattern)
    t = len(text)
    kmp_position = []
    if pattern and text:
        prefix = prefix_table(pattern)
        n = 0 # letter in text
        m = 0 # number of matched letters
        while n < t:
            if text[n] == pattern[m]:
                n += 1
                m += 1
            elif m != 0: # jump to the sufix
                m = prefix[m - 1]
            else:
                n += 1
            if m == p: # pattern found
                kmp_position.append(n - m)
                m = prefix[m - 1]
    return kmp_position

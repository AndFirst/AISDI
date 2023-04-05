def find(pattern, text):
    result = []
    if not (pattern and text):
        return result
    m = len(pattern)
    n = len(text)
    h = pow(256,m-1,100)
    p = 0
    t = 0
    if m>n:
        return result;
    for i in range(m): # we have a hash of the pattern and first m letters of text
        p = (256*p+ord(pattern[i]))%100 # hash of pattern is constant
        t = (256*t+ord(text[i]))%100 # this will change through the for loop
    for s in range(n-m+1):
        if p == t: # if hashes are the same we check letters value by value
            are_same = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    are_same = False
                    break
            if are_same: # if they match each other we add position to the list
                result.append(s)
        if s < n-m: # we are creating hash for next set of letters in the text
            t = (t-h*ord(text[s]))%100 # we subtract hash of the previos first letter
            t = (t*256+ord(text[s+m]))%100 # and add hash of the last letter
            t = (t+100)%100 # in order to t > 0
    return result
# print (find ("xd", "x"))
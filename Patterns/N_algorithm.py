def find(string, text):
    patterns = []
    if not (string and text):
        return patterns
    else:
        for n in range(0, len(text) - len(string) + 1):
            for m in range(0, len(string)):
                if(text[n + m] == string[m]):
                    if m == len(string)-1:
                        patterns.append(n)
                else:
                    break
        return patterns

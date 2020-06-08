def ex5(s):
    index = {}

    i = 0; j = 0

    max_length = 0

    while i < len(s) and j < len(s):
        while j < len(s):
            if s[j] not in index:
                index[s[j]] = j
                if j - i + 1 > max_length:
                    max_length = j - i + 1
            else:
                k = index[s[j]]
                while i <= k:
                    index.pop(s[i])
                    i += 1
                break
            j += 1

    return max_length

# print(ex5("pwwkew"))
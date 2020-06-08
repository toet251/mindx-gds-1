def ex5(s, p):
    def is_ana(count_s, count_p):
        for c in count_s.keys():
            if count_s[c] != count_p[c]:
                return False
        return True 

    count_s = {}
    count_p = {}
    len_p = len(p)

    for c in range(ord('a'), ord('z')+1):
        count_s[chr(c)] = 0
        count_p[chr(c)] = 0

    for c in p:
        count_p[c] += 1

    res = []
    i = 0
    for c in s:
        count_s[c] += 1
        if i >= len_p:
            count_s[s[i-len_p]] -= 1
        
        if i >= len_p-1 and is_ana(count_s, count_p):
            res.append(i-len_p+1)

        i += 1

    return res

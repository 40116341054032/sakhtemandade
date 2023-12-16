def unique(s):
    for j in range(len(s)):
        for k in range(j+1 , len(s)):
            if s[i] == s[k]:
                return False
    return True
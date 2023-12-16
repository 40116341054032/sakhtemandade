def Avg(s):
    n = len(s)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total / (j+1)
    return a
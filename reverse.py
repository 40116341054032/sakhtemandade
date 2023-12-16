def r(a):
    n = len(a)
    for i in range(n//2):
        a[i] , a[n-1-i] = a[n-1-i] , a[i]
    return a
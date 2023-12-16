def f(x , y , n):
    if x > y:
        for i in range(n):
            print(i)
    else:
        for i in range(n):
            for j in range(n):
                print(i,j)
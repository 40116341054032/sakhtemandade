def heapify(x, i):
    p = int((i-1)/2)
    if x[p] > 0:
        if x[i] > x[p]:
            x[i] , x[p] = x[p] , x[i]
            heapify(x , p)

def insertNode(a , d):
    global n
    n += 1
    a.append(d)
    heapify(a , n-1)

c = [45,35,23,27,21,22,4,19]
n = len(c)
insertNode(c , 42)

for i in range(n):
    print(c[i] , end=" ")
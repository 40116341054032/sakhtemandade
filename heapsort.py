def heapify(arr , n ,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr , n , largest)
def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1 , -1 , -1):
        heapify(arr , n , i)
    for i in range(n-1 , 0 , -1):
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr , i ,0)

s = [45,35,23,27,21,22,4,19]
print(s)

heapsort(s)
print(s)
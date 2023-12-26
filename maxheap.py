def heapify(A, n, K):
    left = 2 * K + 1
    right = 2 * K + 2
    if left < n and A[left] > A[K]:
        s = left
    else:
        s = K
    if right < n and A[right] > A[s]:
        s = right
    if s != K:
        A[K], A[s] = A[s], A[K]
        heapify(A, n, s)


def build_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)



arr = [4, 10, 3, 5, 1]
print(arr)

build_max_heap(arr)
print(arr)

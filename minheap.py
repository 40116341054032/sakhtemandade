def heapify(A , K):
    left = 2*K+1
    right = 2*K+2
    if left < len(A) and A[left] < A[K]:
        s = 1
    else:
        s = K
    if right < len(A) and A[right] < A[s]:
        s = right
    if s!= K:
        A[K] , A[s] = A[s] , A[K]
        heapify (A , s)
def build_min_heap(A):
    n = int((len(A)//2) -1)
    for k in range(n , -1 , -1):
        heapify(A , k)
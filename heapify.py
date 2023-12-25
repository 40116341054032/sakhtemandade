def heapify(A , K):
    left = 2*k+1
    right = 2*k+2
    if left < len(A) and A[left] < A[K]:
        s = 1
    else:
        s = K
    if right < len(A) and A[right] < A[s]:
        s = right
    if s!= K:
        A[K] , A[s] = A[s] , A[K]
        heapify (A , s)

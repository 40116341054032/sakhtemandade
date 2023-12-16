def disjoint(A,B,C):
    for a in A:
        for b in B:
            for c in C:
                if (a==b==c):
                    return False
    return True 

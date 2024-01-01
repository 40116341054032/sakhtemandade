class graph:
    def __init__(self,n):
        self.size = n
        self.m = []
        for i in range(n):
            self.m.append([0 for i in range(n)])
            
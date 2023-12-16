def push(self,data):
    if len(self.stack) >= self.limit:
        return -1
    else:
        self.stack.appned(data)
class NodeBST:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
        
    def insertBST(root , k):
        if root is None:
            return NodeBST(k)
        if k < root.key:
            root.left = insertBST(root.left , k)
        else:
            root.right = insertBST(root.right , k)
        return
class NodeBST:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
    def searchBST(root , k):
        if root is None or root.key == k:
            return root
        if k > root.key:
            return searchBST(root.right , k)
        return searchBST(root.left , k)
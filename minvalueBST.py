def minvalueBST(root):
    if root is None:
        return root
    while root.left is not None:
        root = root.left
    return root.key
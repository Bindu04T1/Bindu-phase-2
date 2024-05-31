class TreeNode:
    def __init__(self, data):
        self.val = data 
        self.left = None 
        self.right = None
 
def printInorder(root):
    if root == None:
        return 
    # 1 
    printInorder(root.left)
    # 2 
    print(root.val, end = ", ")
    # 3
    printInorder(root.right)
 
 
def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
def deleteNodeFromBST(root, val):
    if root == None:
        return None 
    elif root.val > val:
        # If root value is greater than node to be deleted
        root.left = deleteNodeFromBST(root.left, val)
    elif root.val < val:
        # If root value is lesser than node to be deleted
        root.right = deleteNodeFromBST(root.right, val)
    else:
        # If root value is equal to node to be deleted
 
        # category-1 (Node with 0 children)
        if root.left == None and root.right == None:
            return None
 
        # category-2 (Node with 1 children) 
        if root.left == None:
            return root.right 
        elif root.right == None:
            return root.left
 
        # category-3 (Node with 2 children)
        # Finding inorder successor 
        curr = root.right 
        while curr.left != None:
            curr = curr.left 
 
        # Once inorder successor is found, we need to replace the value 
        root.val = curr.val 
        root.right = deleteNodeFromBST(root.right, curr.val)
    return root
 
 
 
 
 
 
nums = [10, 8, 12, 5, 23, 20, 43, 23, 11, 7]
root = None
for ele in nums:
    root = insertIntoBST(root, ele)
printInorder(root)
root = deleteNodeFromBST(root, 20)
printInorder(root)

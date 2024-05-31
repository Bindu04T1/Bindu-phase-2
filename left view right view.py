class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
 
 
def printPreorder(root):
    if root == None:
        return 
    # 1 
    print(root.data, end = ", ")
    # 2 
    printPreorder(root.left)
    # 3
    printPreorder(root.right)
 
 
def printInorder(root):
    if root == None:
        return 
    # 1 
    printInorder(root.left)
    # 2 
    print(root.data, end = ", ")
    # 3
    printInorder(root.right)
 
def printPostorder(root):
    if root == None:
        return 
    # 1 
    printPostorder(root.left)
    # 2 
    printPostorder(root.right)
    # 3
    print(root.data, end = ", ")
 
 
 
 
#https://pastebin.com/ugJvxcbL  
 
 
 
# class Solution(object):
#     def maxLevelSum(self, root):
#         if root == None:
#             return 0
#         Q = [root]
#         resultLevel = 0 
#         resultSum = -100000000
#         currLevel = 1
#         while len(Q) > 0:
#             n = len(Q)
#             currSum = 0
#             for i in range(n):
#                 # step-1 (Deleting)
#                 currNode = Q.pop(0)
 
#                 # step-2 (Appending to subResult)
#                 currSum += currNode.val
 
#                 # step-3 (Enquing the left child)
#                 if currNode.left != None:
#                     Q.append(currNode.left)
 
#                 # step-4 (Enquing the right child)
#                 if currNode.right != None:
#                     Q.append(currNode.right)
 
#             if currSum > resultSum:
#                 resultSum = currSum 
#                 resultLevel = currLevel 
#             currLevel += 1
#         return resultLevel 
 
 
def printLevelOrderTraversal(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to subResult)
            subResult.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)    
 
    print(result)
 
def printLeftView(root):
     if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
            if i == 0:
                result.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Left view is:", result)
 
def printRightView(root):
     if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
            if i == n - 1:
                result.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Right view is:", result)
obj1 = Node(12)
obj2 = Node(5)
obj3 = Node(8)
obj4 = Node(-1)
obj5 = Node(2)
obj6 = Node(89)
obj1.left = obj2
obj1.right = obj3 
obj2.left = obj4
obj2.right = obj5
obj3.right = obj6
 
printLeftView(obj1)
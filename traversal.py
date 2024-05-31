def printlevelordertraversal(root):
    if root == None:
        return
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        subresult = []
        for i in range(n):
            currnode=Q.pop(0)
            subresult.append(currnode.data)
            
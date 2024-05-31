class solution(object):
    def preorderHepler(self,root,result):
        if root == None:
            return
        result,append(root.val)
        self.preorderHepler(root.left,result)
        slef.preorderHepler(root.right,result)
    def preorderTraversal(self,root):
        result = []
        self.preorderHepler(root,result)
        return
    
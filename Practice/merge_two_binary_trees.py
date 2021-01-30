class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MergeTrees(object):
    def merge_trees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.merge_trees(t1.left, t2.left)
            root.right = self.merge_trees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

t1 = TreeNode(1,2,3)
t2 = TreeNode(3,4,5)
MergeTrees().merge_trees(t1, t2)

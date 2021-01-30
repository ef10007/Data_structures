# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class RangeSum(object):
    def finding(self, lst, low, high):
        range_sum = 0
        for i in lst:
            if low <= i <= high:
                range_sum += i
        return range_sum


s = RangeSum()
print(s.finding([10,5,15,3,7,13,18,1,6], 6, 10))

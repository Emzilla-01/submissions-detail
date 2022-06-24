# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Runtime: 78 ms, faster than 17.49% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 17.2 MB, less than 31.64% of Python3 online submissions for Closest Binary Search Tree Value.
"""

class Solution:
    def traverse_and_store(self, node: Optional[TreeNode], target:float)->dict:
        if node != None:
            self.d[node.val]=abs(node.val-target)
            self.traverse_and_store(node.left, target), self.traverse_and_store(node.right, target)
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.d=dict()
        self.traverse_and_store(root, target)
        itms=sorted(self.d.items(), key=lambda t: t[1], reverse=0)
        return(itms[0][0])

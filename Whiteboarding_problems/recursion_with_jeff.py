# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        """
        if root is not None:
            return False

        if root.left is None and root.right is None:
            if sum - root.val == 0:
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

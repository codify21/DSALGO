# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    # if root.left is None and root.right is None:
    #     return 1

        def dfs(node, count, max_so_far):

            if node is None:
                return count

            if node.val >= max_so_far:
                max_so_far = node.val
                count = count + 1

            count = dfs(node.left, count, max_so_far)
            count = dfs(node.right, count, max_so_far)

            return count

        return dfs(root, 0, root.val)
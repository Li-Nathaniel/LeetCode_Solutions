# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans = []
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                if root.left == None and root.right == None:
                    ans.append(root.val)
                inOrder(root.right)

        inOrder(root1)
        inOrder(root2) 
        return ans[:len(ans) // 2] == ans[len(ans) // 2:]
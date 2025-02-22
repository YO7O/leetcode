# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        start = cur = 0

        while cur < n and traversal[cur].isdigit():
            cur += 1

        root = TreeNode(int(traversal[start:cur]))
        stack = [(root, 0)]

        while stack and cur < n:
            depth = 0
            while traversal[cur] == '-':
                cur += 1
                depth += 1

            start = cur
            while cur < n and traversal[cur].isdigit():
                cur += 1
            
            node = TreeNode(int(traversal[start:cur]))

            while stack and stack[-1][1] >= depth:
                stack.pop()
            
            if stack[-1][0].left:
                stack[-1][0].right = node
                stack.pop()
            else:
                stack[-1][0].left = node
            
            stack.append((node, depth))
        
        return root
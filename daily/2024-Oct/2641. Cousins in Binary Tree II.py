# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cursum = root.val
        queue = deque([(root, root.val)])
        while queue:
            nextsum = 0
            for i in range(len(queue)):
                node, brosis = queue.pop()
                node.val = cursum - brosis
                left = node.left.val if node.left else 0
                right = node.right.val if node.right else 0
                child = left+right
                nextsum += child
                if node.left:
                    queue.appendleft((node.left, child))
                if node.right:
                    queue.appendleft((node.right, child))
            cursum = nextsum
        return root
                
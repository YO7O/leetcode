# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        if root1.val != root2.val:
            return False

        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            left1 = node1.left.val if node1.left else -1
            left2 = node2.left.val if node2.left else -1
            right1 = node1.right.val if node1.right else -1
            right2 = node2.right.val if node2.right else -1
            if left1 == left2 and right1 == right2:
                if node1.left:
                    stack1.append(node1.left)
                    stack2.append(node2.left)
                if node1.right:
                    stack1.append(node1.right)
                    stack2.append(node2.right)
            elif left1 == right2 and right1 == left2:
                if node1.left:
                    stack1.append(node1.left)
                    stack2.append(node2.right)
                if node1.right:
                    stack1.append(node1.right)
                    stack2.append(node2.left)
            else:
                return False
        return True

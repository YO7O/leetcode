# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def appendHelper(lst: List[TreeNode], node: TreeNode) -> None:
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)

        even = deque([root])
        odd = deque([])

        while even:
            while even:
                node = even.popleft()
                appendHelper(odd, node)

            l = 0
            r = len(odd) - 1
            while l < r:
                lnode = odd[l]
                rnode = odd[r]
                lnode.val, rnode.val = rnode.val, lnode.val
                l += 1
                r -= 1

            while odd:
                node = odd.popleft()
                appendHelper(even, node)
            
        return root
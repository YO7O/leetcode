# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [[root], []]
        ans = []
        while level[0]:
            maxx = -sys.maxsize-1
            while level[0]:
                node = level[0].pop()
                maxx = max(maxx, node.val)
                if node.left:
                    level[1].append(node.left)
                if node.right:
                    level[1].append(node.right)
            ans.append(maxx)
            level.reverse()
        return ans
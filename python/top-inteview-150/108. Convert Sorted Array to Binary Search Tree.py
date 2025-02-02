# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(start: int, end: int) -> Optional[TreeNode]:
            if end-start == 0:
                return None 
            if end-start == 1:
                return TreeNode(nums[start])
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid)
            root.right = dfs(mid+1, end)
            return root

        return dfs(0, len(nums))

# slower in python but should be fine on language where pointer exist

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if len(nums) == 0:
#             return None
#         if len(nums) == 1:
#             return TreeNode(nums[0])
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root
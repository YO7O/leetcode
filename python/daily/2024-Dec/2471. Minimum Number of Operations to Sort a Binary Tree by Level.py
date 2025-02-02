# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        cur = deque([root])
        nextt = deque([])
        ans = 0
        while cur:
            nums = []
            i = 0
            poss = {}
            while cur:
                node = cur.popleft()
                if node.left:
                    nextt.append(node.left)
                if node.right:
                    nextt.append(node.right)

                nums.append(node.val)
                poss[node.val] = i
                i += 1
            
            sortNums = sorted(nums)
            for j in range(i):
                if sortNums[j] != nums[j]:
                    ogPos = poss[sortNums[j]]
                    nums[j], nums[ogPos] = nums[ogPos], nums[j]
                    poss[nums[j]], poss[nums[ogPos]] = j, ogPos
                    ans += 1
            
            cur, nextt = nextt, cur

        return ans
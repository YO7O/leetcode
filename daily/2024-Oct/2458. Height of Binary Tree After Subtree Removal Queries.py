# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def heightFind(node: TreeNode, level: int) -> int:
            leftHeight = heightFind(node.left, level+1) if node.left else level
            rightHeight = heightFind(node.right, level+1) if node.right else level
            self.nodes[node.val] = node
            self.leftHeight[node.val] = leftHeight
            self.rightHeight[node.val] = rightHeight
            return max(leftHeight, rightHeight)
        
        def heightWO(node: TreeNode) -> None:
            if node.left:
                self.heightWithout[node.left.val] = max(self.heightWithout[node.val], self.rightHeight[node.val])
                heightWO(node.left)
            if node.right:
                self.heightWithout[node.right.val] = max(self.heightWithout[node.val], self.leftHeight[node.val])
                heightWO(node.right)

        self.nodes = [None] * 100001
        self.leftHeight = [0] * 100001
        self.rightHeight = [0] * 100001
        self.heightWithout = [0] * 100001
        heightFind(root, 0)
        heightWO(root)
        ans = []
        for q in queries:
            ans.append(self.heightWithout[q])
        return ans
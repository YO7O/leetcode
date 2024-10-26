class TreeNode:
    def __init__(self, child, string="", isdir=False):
        self.string = string
        self.isdir = isdir
        self.child = child

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sorting folder ended up being better, probably because it is O(10000 n) while sorting is O(n log n)
        # and there's no system optimization
        root = TreeNode({}, "/")
        for f in folder:
            left = 0
            right = 1
            curnode = root
            while right < len(f):
                if f[right] == '/':
                    string = f[:right]
                    if string not in curnode.child:
                        curnode.child[string] = TreeNode({}, string)
                    curnode = curnode.child[string]
                    left = right
                    if curnode.isdir:
                        break
                right += 1
            if curnode.isdir:
                continue
            if f not in curnode.child:
                curnode.child[f] = TreeNode({}, f, True)
            else:
                curnode = curnode.child[f]
                curnode.isdir = True
                curnode.child = {}

        ans = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.isdir:
                ans.append(node.string)
            for c in node.child:
                queue.append(node.child[c])

        return ans
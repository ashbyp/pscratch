from typing import Optional
from typing import List
from utils.measure import checker
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = [root]

        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            ans.append(level)
        return ans

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        k = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            k[level].append(node.val)
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)

        dfs(root, 0)
        return [i for i in k.values()]


if __name__ == '__main__':
    three = TreeNode(val = 3)
    nine = TreeNode(val=9)
    twenty = TreeNode(val=20)
    fifteen = TreeNode(val=15)
    seven = TreeNode(val=7)

    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven

    with checker(Solution().levelOrder1, repeat=100000, check_success=True) as c:
        c.check_1(three, [[3], [9, 20], [15, 7]])
    with checker(Solution().levelOrder2, repeat=100000, check_success=True) as c:
        c.check_1(three, [[3], [9, 20], [15, 7]])


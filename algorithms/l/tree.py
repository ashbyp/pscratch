from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

    def insert(self, tree: TreeNode, val: int):
        if val < tree.val:
            if tree.left:
                self.insert(tree.left, val)
            else:
                tree.left = TreeNode(val)
        else:
            if tree.right:
                self.insert(tree.right, val)
            else:
                tree.right = TreeNode(val)

    def build_tree(self, vals: list[int]) -> TreeNode:
        if not vals:
            return None
        root = TreeNode(vals[0])
        for val in vals[1:]:
            self.insert(root, val)
        return root

    def print_tree(self, root: TreeNode):
        if root:
            print(root.val, end=' ')
            self.print_tree(root.left)
            self.print_tree(root.right)


def main():
    s = Solution()
    t = s.build_tree([4,2,7,1,3,6,9])
    s.print_tree(t)
    print()
    s.invertTree(t)
    s.print_tree(t)


if __name__ == '__main__':
    main()
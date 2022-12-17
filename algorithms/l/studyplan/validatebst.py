from typing import Optional

from utils.measure import checker


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            left = valid(node.left, left, node.val)
            right = valid(node.right, node.val, right)
            return left and right

        return valid(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    with checker(Solution().isValidBST, repeat=0, check_success=True) as c:
        one = TreeNode(1)
        two = TreeNode(2)
        three = TreeNode(3)
        two.left = one
        two.right = three
        c.check_1(two, True)


        one = TreeNode(1)
        three = TreeNode(3)
        four = TreeNode(1)
        five = TreeNode(1)
        six = TreeNode(1)
        five.left = one
        five.right = four
        four.left = three
        four.right = six
        c.check_1(five, False)

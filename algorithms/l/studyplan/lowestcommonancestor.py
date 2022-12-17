from typing import Optional

from utils.measure import checker


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur

if __name__ == '__main__':
    with checker(Solution().lowestCommonAncestor, repeat=0, check_success=True) as c:
        zero = TreeNode(0)
        one = TreeNode(1)
        two = TreeNode(2)
        three = TreeNode(3)
        four = TreeNode(4)
        five = TreeNode(5)
        six = TreeNode(6)
        seven = TreeNode(7)
        eight = TreeNode(8)
        nine = TreeNode(9)

        six.left, six.right = two, eight
        two.left, two.right = zero, four
        eight.left, eight.right = seven, nine
        four.left, four.right = three, five

        c.check_3(six, two, eight, six)
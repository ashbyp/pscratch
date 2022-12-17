from typing import List
from utils.measure import checker


class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def preorder1(self, root: Node) -> List[int]:
        nodes = []

        def traverse(node):
            if node:
                nodes.append(node.val)
                for n in node.children:
                    traverse(n)

        traverse(root)
        return nodes

    def preorder2(self, root: Node) -> List[int]:
        stack = []
        nodes = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                nodes.append(node.val)
                for n in node.children[::-1]:
                    stack.append(n)
        return nodes


if __name__ == '__main__':
    with checker(Solution().preorder1, repeat=1000, check_success=True) as c:
        nodes = []
        for val in range(1, 7):
            nodes.append(Node(val=val))
        nodes[2].children = [nodes[4], nodes[5]]
        nodes[0].children = [nodes[2], nodes[1], nodes[3]]
        c.check_1(nodes[0], [1,3,5,6,2,4])
    with checker(Solution().preorder2, repeat=1000, check_success=True) as c:
        nodes = []
        for val in range(1, 7):
            nodes.append(Node(val=val))
        nodes[2].children = [nodes[4], nodes[5]]
        nodes[0].children = [nodes[2], nodes[1], nodes[3]]
        c.check_1(nodes[0], [1, 3, 5, 6, 2, 4])

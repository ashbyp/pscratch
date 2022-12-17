class Node:
    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def left(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


def create_tree():
    #           10
    #      12          7
    #    5    11    3    13

    n = Node(10)
    n.left = Node(12)
    n.left.left = Node(5)
    n.left.right = Node(11)
    n.right = Node(7)
    n.right.left = Node(3)
    n.right.right = Node(130)
    return n


def max_sum_to_leaf(n):
    # if not n:
    #     return 0

    ls = 0 if not n.left else max_sum_to_leaf(n.left)
    rs = 0 if not n.right else max_sum_to_leaf(n.right)

    return ls + n.value if ls > rs else rs + n.value


def print_tree(n):
    if not n:
        return
    print_tree(n.left)
    print(n.value)
    print_tree(n.right)


if __name__ == '__main__':
    tree = create_tree()
    print_tree(tree)
    print(max_sum_to_leaf(tree))


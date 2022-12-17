class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_tree():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    g.right = h
    return a


def diameter(tree):
    dia = [0]

    def search(root):
        if not root:
            return -1

        left = search(root.left)
        right = search(root.right)
        dia[0] = max(dia[0],  2 + left + right)

        return 1 + max(left, right)

    search(tree)
    return dia[0]


def diameter1(tree):
    if tree is None:
        return 0
    res = [0]

    def traverse(root):
        if root is None:
            return 0
        left = traverse(root.left)
        right = traverse(root.right)
        if left + right > res[0]:
            res[0] = left + right
        return max(left, right) + 1

    traverse(tree)
    return res[0]


def main():
    print(diameter(create_tree()))
    print(diameter1(create_tree()))
    tree = create_tree()
    print(diameter(tree.right))
    print(diameter1(tree.right))
    print(diameter(tree.left))
    print(diameter1(tree.left))
    print(diameter(tree.left.left))
    print(diameter1(tree.left.left))


if __name__ == '__main__':
    main()

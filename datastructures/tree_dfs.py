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


def walk_preorder(tree):
    if tree:
        print(tree.value, end=' ')
        walk_preorder(tree.left)
        walk_preorder(tree.right)


def walk_inorder(tree):
    if tree:
        walk_inorder(tree.left)
        print(tree.value, end=' ')
        walk_inorder(tree.right)


def walk_postorder(tree):
    if tree:
        walk_postorder(tree.left)
        walk_postorder(tree.right)
        print(tree.value, end=' ')


def itwalk_preorder(tree, stack):
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node:
            print(node.value, end=' ')
            stack.append(node.right)
            stack.append(node.left)


def itwalk_inorder(tree, stack):
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.right)
            print(node.value, end=' ')
            stack.append(node.left)


def itwalk_postorder(tree, stack):
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.right)
            stack.append(node.left)
            print(node.value, end=' ')


def height(tree):
    print(f'Node: {tree.value if tree else "None"}')
    if not tree:
        return -1

    left = height(tree.left)
    right = height(tree.right)

    print(f' will return {1 + max(left, right)}')

    return 1 + max(left, right)


def main():
    root = create_tree()
    print('Pre-order')
    walk_preorder(root)
    print()
    print(f'Height is {height(root)}')


    print()
    print('In-order')
    walk_inorder(root)
    print()
    print('Post-order')
    walk_postorder(root)
    print()

    print('Iterative Pre-order')
    itwalk_preorder(root, [])
    print()
    print('Iterative In-order')
    itwalk_inorder(root, [])
    print()
    print('Iterative Post-order')
    itwalk_postorder(root, [])
    print()

if __name__ == '__main__':
    main()
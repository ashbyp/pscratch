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


def bfs(root: Node):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node.value)

        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)


def main():
    root = create_tree()
    bfs(root)


if __name__ == '__main__':
    main()

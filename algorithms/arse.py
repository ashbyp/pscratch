

class Node:

    def __init__(self, value: int, next_node: 'Node|None') -> None:
        self.value = value
        self.next = next_node


def print_list(root: Node) -> None:
    ptr = root
    while ptr:
        print(ptr.value)
        ptr = ptr.next
    print()


def build(numbers: list[int]) -> Node:
    first = Node(0, None)
    ptr = first
    for n in numbers:
        node = Node(n, None)
        ptr.next = node
        ptr = ptr.next
    return first.next


if __name__ == '__main__':
    l = build([3, 2, 10, 1])
    print_list(l)



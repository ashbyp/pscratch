class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'({self.key}:{self.val} p={self.prev.val} n={self.next.val})'

    def __repr__(self):
        return self.__str__()


class LRUCache:

    def __init__(self, capacity=4):
        self.capacity = capacity
        self.d = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, key, val):
        if self.contains(key) or len(self.d) >= self.capacity:
            self.remove(self.tail.prev.key)

        n = Node(key, val)
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n
        self.d[key] = n

    def remove(self, key):
        n = self.d[key]
        n.prev.next = n.next
        n.next.prev = n.prev
        del self.d[key]

    def get(self, key):
        n = self.d[key]
        self._update_used(n)
        return n.val

    def contains(self, key):
        return key in self.d

    def debug(self):
        print('------')
        print(self.d)
        curr = self.head.next
        while curr != self.tail:
            print(curr)
            curr = curr.next

    def _update_used(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = self.head
        n.next = self.head.next
        self.head.next.prev = n
        self.head.next = n


if __name__ == '__main__':
    c = LRUCache()
    c.debug()
    c.add('a', 10)
    c.debug()
    c.add('b', 20)
    c.debug()
    c.add('c', 30)
    c.debug()
    c.add('d', 40)
    c.debug()
    c.remove('c')
    c.debug()
    c.remove('b')
    c.debug()
    c.remove('a')
    c.debug()
    c.remove('d')
    c.debug()

    c.add('a', 10)
    c.add('b', 20)
    c.add('c', 30)
    c.add('d', 40)
    c.debug()

    print(f'Get c == {c.get("c")}')
    c.debug()

    c.add('e', 100)
    c.debug()
    print(f'Get b == {c.get("b")}')
    c.debug()
    c.add('f', 1000)
    c.debug()

    print([f'{x}=={c.contains(x)}' for x in ('a', 'b', 'c', 'd','e', 'f')])

    c.add('e', 1000000)
    c.debug()
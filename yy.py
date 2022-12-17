
class RandMap:

    def __init__(self):
        self.d = {}
        self.l = []

    def add(self, val):
        if not val in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)

    def remove(self, val):
        pos = self.d[val]
        mov = self.l.pop()
        self.l[pos] = mov
        del self.d[val]
        self.d[mov] = pos

    def contains(self, val):
        return val in self.d

    def rand(self):
        import random
        return random.choice(self.l)

    def __len__(self):
        assert len(self.d) == len(self.l)
        return len(self.d)


if __name__ == '__main__':
    r = RandMap()
    for s in 'the quick brown fox jumped over the lazy hen'.split(' '):
        r.add(s)

    print(r.d)
    print(r.l)

    print(f'Len: {len(r)}')
    print(f'quick {r.contains("quick")}')
    print(f'blue {r.contains("blue")}')
    for _ in range(5):
        print(f'Rand: {r.rand()}')

    r.remove('quick')
    print(f'Len: {len(r)}')
    print(f'quick {r.contains("quick")}')

    print(r.d)
    print(r.l)

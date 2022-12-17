import threading


class Randmap:

    def __init__(self):
        self.d = {}
        self.l = []
        self.lock = threading.Lock()

    def add(self, val):
        with self.lock:
            self.l.append(val)
            self.d[val] = len(self.l) - 1

    def contains(self, val):
        return val in self.d

    def remove(self, val):
        with self.lock:
            pos = self.d[val]
            self.l[pos] = self.l.pop()
            self.d[self.l[pos]] = pos
            del self.d[val]

    def print(self):
        print(self.l)
        print(self.d)

    def getrand(self):
        import random
        return random.choice(self.l)


if __name__ == '__main__':
    r = Randmap()
    r.add('my')
    r.add('name')
    r.add('is')
    r.add('paul')
    r.print()

    for i in range(3):
        print(r.getrand())

    r.remove('name')
    r.print()

    for i in range(3):
        print(r.getrand())

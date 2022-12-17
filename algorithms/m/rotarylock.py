# You're trying to open a lock. The lock comes with a wheel which has the integers from 1 to N arranged in a circle
# in order around it (with integers 1 and N adjacent to one another). The wheel is initially pointing at 1.

# It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in either direction, and it takes no time to
# select an integer once the wheel is pointing at it.
# The lock will open if you enter a certain code. The code consists of a sequence of M integers, the ith of which is
# C{i}

#  Determine the minimum number of seconds required to select all M of the code's integers in order.
from typing import List


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Lock:
    def __init__(self, numbers):
        self.loc = Node(numbers[0])
        current = self.loc
        for x in range(1, len(numbers)):
            node = Node(numbers[x])
            current.next = node
            node.prev = current
            current = node
        current.next = self.loc
        self.loc.prev = current

    def goto(self, new_val) -> int:
        loc = self.loc
        fwd_seconds = 0
        bwd_seconds = 0

        while loc.val != new_val:
            fwd_seconds += 1
            loc = loc.next

        loc = self.loc
        while loc.val != new_val:
            bwd_seconds += 1
            loc = loc.prev

        self.loc = loc
        return min(fwd_seconds, bwd_seconds)

class Lock1:

    def __init__(self, numbers):
        self.loc = 0
        self.numbers = numbers


    def goto(self, new_val) -> int:
        # print(f'goto {new_val}')
        loc = self.loc
        fwd_seconds = 0
        bwd_seconds = 0

        while self.numbers[loc] != new_val:
            fwd_seconds += 1
            loc = (loc + 1) % len(self.numbers)

        loc = self.loc
        # print(f'start {loc}')
        while self.numbers[loc] != new_val:
            # print(f'loop {loc}')
            bwd_seconds += 1
            loc = loc - 1
            # print(f'loc {loc}')
            if loc == -1:
                # print('reset')
                loc = len(self.numbers)-1


        self.loc = loc
        return min(fwd_seconds, bwd_seconds)


class Lock2:

        def __init__(self, numbers):
            self.loc = 1
            self.N = numbers[-1]

        def goto(self, new_val) -> int:
            if new_val == self.loc: return 0

            if new_val > self.loc:
                fwd_seconds = new_val - self.loc
                bwd_seconds = self.loc - new_val
                if bwd_seconds < 0:
                    bwd_seconds = self.N + bwd_seconds
            else:
                bwd_seconds = self.loc - new_val
                fwd_seconds = new_val - self.loc
                if fwd_seconds < 0:
                    fwd_seconds = self.N + fwd_seconds

            self.loc = new_val
            return min(fwd_seconds, bwd_seconds)


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    l = Lock2(list(range(1, N+1)))
    seconds = 0
    for c in C:
        seconds += l.goto(c)
    return seconds


if __name__ == '__main__':
    print(getMinCodeEntryTime(3, 3, [1, 2, 3]))
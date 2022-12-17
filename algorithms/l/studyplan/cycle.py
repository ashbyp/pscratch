from typing import Optional
from utils.measure import checker


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make(l: list[int], pos=1) -> ListNode | None:
    head = ListNode()
    curr = head
    i = 0
    backptr = None

    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            backptr = curr
        i += 1

    if backptr:
        curr.next = backptr
    return head.next


def unmake(ln: ListNode | None) -> list[int]:
    return ln.val if ln else -1


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            visited = set()
            while head:
                visited.add(head)
                if head.next in visited:
                    return head.next
                head = head.next
        return None

    def wrapped(self, l, pos):
        return unmake(self.detectCycle(make(l, pos)))


def main():
    with checker(Solution().wrapped) as c:
        c.check_2([3,2,0,-4], 1, 2)
        c.check_2([1, 2], 0, 1)
        c.check_2([1], -1, -1)


if __name__ == '__main__':
    main()



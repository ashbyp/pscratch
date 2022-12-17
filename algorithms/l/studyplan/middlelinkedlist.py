from typing import Optional
from utils.measure import checker


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printl(l: ListNode) -> None:
    while l:
        print(l.val, end=' ')
        l = l.next
    print('')


def make(l: list[int]) -> ListNode | None:
    head = ListNode()
    curr = head

    for val in l:
        curr.next = ListNode(val)
        curr = curr.next

    return head.next


def unmake(ln: ListNode | None) -> list[int]:
    res = []
    while ln:
        res.append(ln.val)
        ln = ln.next
    return res


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        m = l // 2 + 1

        curr = head
        l = 1
        while curr:
            if l == m:
                return curr
            l = l + 1
            curr = curr.next



    def wrapped(self, list1: list[int]) -> list[int]:
        return unmake(self.middleNode(make(list1)))


if __name__ == '__main__':
    with checker(Solution().wrapped, repeat=0, check_success=True) as c:
        c.check_1([1, 2, 3, 4, 5], [3, 4, 5])
        c.check_1([1, 2, 3, 4, 5, 6], [4, 5, 6])
        c.check_1([1], [1])


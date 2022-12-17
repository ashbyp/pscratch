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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        curr = merged

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return merged.next

    def wrapped(self, list1: list[int], list2: list[int]) -> list[int]:
        return unmake(self.mergeTwoLists(make(list1), make(list2)))


if __name__ == '__main__':
    with checker(Solution().wrapped, repeat=0, check_success=True) as c:
        c.check_2([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
        c.check_2([], [], [])
        c.check_2([], [0], [0])
        c.check_2([1, 2, 4, 6, 7, 8], [1, 3, 4], [1, 1, 2, 3, 4, 4, 6, 7, 8])

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def print(self, head: ListNode) -> None:
        while head:
            print(head.val, end= ' ')
            head = head.next
        print()

    def make(self, vals: list[int]) -> ListNode:
        head, curr = None, None
        for val in vals:
            if not head:
                head = ListNode(val)
                curr = head
            else:
                curr.next = ListNode(val)
                curr = curr.next
        return head


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, curr = None, None
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    if not head:
                        head = ListNode(list1.val)
                        curr = head
                    else:
                        curr.next = ListNode(list1.val)
                        curr = curr.next
                    list1 = list1.next
                else:
                    if not head:
                        head = ListNode(list2.val)
                        curr = head
                    else:
                        curr.next = ListNode(list2.val)
                        curr = curr.next
                    list2 = list2.next
            else:
                remain = list1 or list2
                if curr:
                    curr.next = remain
                else:
                    curr = remain
                break

        return head

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


def main():
    s = Solution()
    l = s.make([1,2,4,6,7])
    s.print(l)
    r = s.reverseList(l)
    s.print(r)

    print('Merge')
    l1 = s.make([1,2,2, 3, 4, 4])
    l2 = s.make([1,3,4])
    s.print(l1)
    s.print(l2)
    s.print(s.mergeTwoLists(l1, l2))


if __name__ == '__main__':
    main()

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers_first(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        l1_curr = l1
        l2_curr = l2
        ans_curr = ans

        while l1_curr or l2_curr or carry:
            if l1_curr:
                l1_curr = l1_curr.next
            if l2_curr:
                l2_curr = l2_curr.next

            if l1_curr and l2_curr:
                ans_curr.next = ListNode((l1_curr.val + l2_curr.val + carry) % 10)
                carry = (l1_curr.val + l2_curr.val + carry) // 10
                ans_curr = ans_curr.next
            elif l1_curr:
                ans_curr.next = ListNode((l1_curr.val + carry) % 10)
                carry = (l1_curr.val + carry) // 10
                ans_curr = ans_curr.next
            elif l2_curr:
                ans_curr.next = ListNode((l2_curr.val + carry) % 10)
                carry = (l2_curr.val + carry) // 10
                ans_curr = ans_curr.next
            elif carry:
                ans_curr.next = ListNode(carry % 10)
                carry = 0 # stop
                ans_curr = ans_curr.next

        return ans

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result

        while l1 or l2 or carry:
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0

            summation = first_num + second_num + carry

            num = summation % 10
            carry = summation // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


    def create(self, l1, l2):
        ll1 = ListNode(l1[0])
        curr = ll1
        for n in l1[1:]:
            curr.next = ListNode(n)
            curr = curr.next

        ll2 = ListNode(l2[0])
        curr = ll2
        for n in l2[1:]:
            curr.next = ListNode(n)
            curr = curr.next

        return ll1, ll2

    def print(self, ll):
        while ll:
            print(ll.val, end=', ')
            ll = ll.next
        print()


if __name__ == '_///_main__':
    s = Solution()

    ll1, ll2 = s.create([2, 3], [5, 4])
    s.print(ll1)
    s.print(ll2)
    s.print(s.addTwoNumbers(ll1, ll2))  # expecting 7, 7

    ll1, ll2 = s.create([2, 4, 3], [5, 6, 4])
    s.print(ll1)
    s.print(ll2)
    s.print(s.addTwoNumbers(ll1, ll2)) # expecting 7, 0, 8

    ll1, ll2 = s.create([9,9,9,9,9,9,9], [9,9,9,9])
    s.print(ll1)
    s.print(ll2)
    s.print(s.addTwoNumbers(ll1, ll2))  # expecting [8,9,9,9,0,0,0,1]


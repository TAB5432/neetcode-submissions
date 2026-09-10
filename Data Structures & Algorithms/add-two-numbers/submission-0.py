# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""

        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        
        
        num1, num2 = num1[::-1], num2[::-1]
        num1, num2 = int(num1), int(num2)
        res = num1 + num2
        res = str(res)
        res = res[::-1]

        def string_to_list(string):
            prev = None
            first = None
            for i in string:
                curr = ListNode(i)
                if not first:
                    first = curr
                if prev:
                    prev.next = curr
                prev = curr
            return first
        
        return string_to_list(res)




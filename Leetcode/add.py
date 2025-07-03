# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Method to print the linked list
    def display(self):
        current = self
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print()

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next

# Helper function to create linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Create two numbers: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
result.display()  # Output: 7 -> 0 -> 8

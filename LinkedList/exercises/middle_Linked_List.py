from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


#Test Case
#1
#head = [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = middleNode(head)
print(f'The middle node is : {result}')

#1
#head = [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

result = middleNode(head)
print(f'The middle node is : {result}')
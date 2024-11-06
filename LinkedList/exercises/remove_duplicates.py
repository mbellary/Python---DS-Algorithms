from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head: Optional[ListNode]) -> Optional[ListNode] :
    if not head:
        return

    dummy = head
    while dummy:
        if not dummy.next:
            return head
        next_node = dummy.next
        while dummy.val == next_node.val:
            dummy.next = dummy.next.next
            next_node = dummy.next
            if not next_node:
                return head
        dummy = dummy.next

    return head

def getNodes(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans

#Test Case
#1
#head = [1, 1, 2]
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
head = node1
node1.next = node2
node2.next = node3

result = getNodes(removeDuplicates(head))
print(f'Linked list without duplicates : {result}')

#2
#head = [1, 1, 2, 3, 3]
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = getNodes(removeDuplicates(head))
print(f'Linked list without duplicates : {result}')

#1
#head = [1, 1, 1]
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
head = node1
node1.next = node2
node2.next = node3

result = getNodes(removeDuplicates(head))
print(f'Linked list without duplicates : {result}')
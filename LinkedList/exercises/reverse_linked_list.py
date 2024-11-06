from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

    if left == right:
        return head

    prev = None
    left_node = None
    curr = head
    index = 1

    while curr:
        next_node = curr.next

        if index == left:
            left_node = curr
            prev = curr
            curr = next_node
            next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        if index == right:
            left_node = next_node
            head.next = curr
        index = index + 1


    return prev


def get_nodes(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans

#Test Case
1
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

result = reverseBetween(head, 2, 4)
result = get_nodes(result)
print(f'The reversed list : {result}')
#
# #2
# node5 = ListNode(5)
# head = node5
# result = reverseBetween(head, 1, 1)
# result = get_nodes(result)
# print(f'The reversed list : {result}')
#
# #3
# node3 = ListNode(3)
# node5 = ListNode(5)
# head = node3
# node3.next = node5


# result = reverseBetween(head, 1, 2)
# result = get_nodes(result)
# print(f'The reversed list : {result}')
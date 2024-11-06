class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


#Refrence to the head is lost and head will be the lost node of the linked list
def get_sum(head):
    ans = 0

    while head:
        ans += head.val
        head = head.next

    return ans, head

# With dummy pointer reference is maintained .
def get_sum_dummy(head):
    ans = 0
    dummy = head

    while dummy:
        ans += dummy.val
        dummy = dummy.next

    return ans, dummy , head

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(1)
four.next = two
one.next = two
two.next = three
head = one

print( one.val == four.val)
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)

# a, h = get_sum(head)
# print(a)
# print(h.val)
# print(h.next)

# a, d, h = get_sum_dummy(head)
# print(a)
# print(h.val)
# print(h.next.val)
# print(h.next.next.val)
# print(d.val)
# print(d.next)

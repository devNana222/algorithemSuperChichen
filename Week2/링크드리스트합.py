class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = 0
    h1 = linked_list_1.head
    while h1 is not None:
        sum1 = sum1* 10 + h1.data
        h1 = h1.next

    sum2 = 0
    h2 = linked_list_2.head
    while h2 is not None:
        sum2 = sum2* 10 + h2.data
        h2 = h2.next
    return sum1 + sum2




linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
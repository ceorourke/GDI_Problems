class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def nth_node_from_end(self, n):
        """Takes the head of a singly Linked List and 
           a number n and returns the nth node from the end of the LL"""

        length = 0

        if self.head:
            current = self.head
            while current:
                length += 1
                current = current.next

            count = 0
            current = self.head
            while count < (length - n): 
                count += 1
                current = current.next
            return current.data

ll = LinkedList()
ll.append_node(1)
ll.append_node(2)
ll.append_node(3)
ll.append_node(4)
ll.append_node(5)

# ll.print_list()
print ll.nth_node_from_end(3)
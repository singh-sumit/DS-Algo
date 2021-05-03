# Given a singly linked list , convert it into circular linked list.
"""
Idea :
    - Traverse and find a last node pointing to None,
    - Update last node's next to starting head node
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:

    # constructor
    def __init__(self):
        self.head = None

    # push a node to list       --O(1)
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # display node in list      --O(n)
    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next  # update curr pointer
        print("None")

    # function to convert linked list into circular list        --O(n)
    def convert_to_circular(self):
        # find last node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        # got a last node, update next
        curr.next = self.head
        return self.head

    # function to display circular list         --O(n)
    def print_circular(self, c_head):
        curr = c_head
        # if c_list has element
        if c_head is not None:
            # keep traversing until first node is reached again
            while True:
                print(curr.data, end=" -> ")
                curr = curr.next
                if curr is c_head:
                    print(curr.data)
                    break
        else:
            print("No element to display in circular list.")


# code execution begins here
if __name__ == "__main__":
    llist = LinkedList()
    llist.print_list()

    # add element to list
    for elem in [47, 2, 90, 69]:
        llist.push(elem)

    llist.print_list()

    # convert to circular
    circ_head = llist.convert_to_circular()

    print("Circular list is")
    llist.print_circular(circ_head)

# Split a Circular Linked List into Two Halves
# If there are odd numbers of nodes, then first list contains one extra nodes.
"""
1. Find the mid and last pointer using Tortrise and Hare algorithm.
2. Make second Half circular
3. Make first half circular
4. Set each head to start of each sub-list
"""


# Node class
class Node:

    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular List class
class CircularList:

    # constructor
    def __init__(self):
        self.head = None

    # insert node at begin of list          --O(1)
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head

        # head is not initialized yet
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            # find last node by traversing and set its next to new_node
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            temp.next = new_node
            self.head = new_node

    # split a list into two halves
    def split_list(self, head1, head2):

        # slow-fast pointer algo
        slow_ptr = self.head
        fast_ptr = self.head

        while (fast_ptr.next != self.head) and (fast_ptr.next.next != self.head):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # if there are even numbers of elements in list move fast_ptr
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

        # set the head pointer of first half
        head1.head = self.head

        # set the head pointer of second half
        head2.head = slow_ptr.next

        # make second half circular
        fast_ptr.next = slow_ptr.next

        # make first half circular
        slow_ptr.next = self.head

    # display nodes in circular list
    def print_list(self):
        curr = self.head

        if self.head is not None:
            while True:
                print("%d" % curr.data, end=' -> ')
                curr = curr.next
                if curr is self.head:
                    print()
                    break
        else:
            print('Nothing to display')


# Code execution begins here
if __name__ == "__main__":
    clist = CircularList()
    clist.print_list()

    # add elements
    clist.push(5)
    clist.push(4)
    clist.push(3)
    clist.push(2)
    clist.push(1)

    print("Original Circular Linked List")
    clist.print_list()

    # split the list
    clist1 = CircularList()
    clist2 = CircularList()

    clist.split_list(clist1, clist2)

    print("First half :")
    clist1.print_list()

    print("Second Half :")
    clist2.print_list()



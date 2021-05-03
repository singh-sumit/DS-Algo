# Delete a node from circular linked list
"""
Algorithm:
Case 1: List is empty
    1. If list is empty we return simply
Case 2: List is not empty
    1. Define two pointer curr, prev where
        curr = head
        prev = None
    2. Traverse through list until a node with deletable element is found
        Until then move
        prev = curr
        curr = curr.next
    3. If prev is still None then deletable node is head.
        So, set head = curr.next
        and find last node and set it to new head node
    4. Else,
        Set prev.next = curr.next
"""


# node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# circular list class
class CircularLinkedList:

    def __init__(self):
        self.head = None

    # push a node to head of list           --O(n)
    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head

            # find a last node and update its next
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            # temp is last node then
            temp.next = new_node  # create loop
        else:
            new_node.next = new_node  # create self loop
        # update head
        self.head = new_node

    # delete a node from a list         -- O(n)
    def delete(self, value):
        if self.head is None:
            print("No element in list. Unable to delete.")
            return
        else:
            prev = None
            curr = self.head

            # find a node with value to be delete
            while (curr.data != value):
                prev = curr
                curr = curr.next
                # if reached searching again same first node
                if curr is self.head:
                    break

            # at this point prev points a node before a deletable node
            # or is still None; ie. either first element is deletable node
            if curr.data == value:
                # to delete head node data
                if prev is None:
                    # find a last node and update its next
                    temp = self.head

                    while temp.next is not self.head:
                        temp = temp.next

                    if temp is self.head:
                        self.head = None
                    else:
                        temp.next = curr.next
                        # update head to next of curr node
                        self.head = curr.next
                else:
                    prev.next = curr.next
            else:
                print("No node with value:", value, " found.")

    # print item in list            ---O(n)
    def print_list(self):
        curr = self.head
        # if list has element
        if self.head is not None:
            while True:
                print(curr.data, end=" -> ")
                curr = curr.next
                if curr is self.head:
                    print()
                    break
        else:
            # if list has no element
            print("No node in list.")


# Code execution begins here
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.print_list()

    # add element to list
    for elem in [4, 92, 50, 24, 88]:
        clist.push(elem)

    clist.print_list()

    # Deletion
    print("Deletion")
    clist.delete(92)
    print("After deletion ", 92)
    clist.print_list()

    clist.delete(4)
    print("After deletion :", 4)
    clist.print_list()

    clist.delete(88)
    print("After deletion: ", 88)
    clist.print_list()

    clist.delete(50)
    print("After deletion :", 50)
    clist.print_list()

    clist.delete(100)
    print("after deletion :", 100)
    clist.print_list()

    clist.delete(24)
    print("After deletion :", 24)
    clist.print_list()
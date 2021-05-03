# Given a singly linked list, detect whether it is a circular or not
# A linked list is not circular if NULL-terminated

# Can use - CYCLE DETECTION ALGORITHM

# class Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class List:

    def __init__(self):
        self.head = None

    def detect_loop(self):
        curr = self.head
        while True:
            if curr is None:
                return False  # either is linked list or circular list is not initalized
            elif curr.next is self.head:
                return True
            curr = curr.next  # update curr


# Circular Linked List class
class CircularLinkedList(List):

    def __init__(self):
        self.head = None

    # push node to head     --O(1)
    def push(self, value):
        new_node = Node(value)

        # if has element then find last element and set next to new_node
        if self.head is not None:
            temp = self.head
            while (temp.next is not self.head):
                temp = temp.next
            # temp is pointing to last node
            temp.next = new_node  # created a loop

            new_node.next = self.head
        else:
            # if list is not initialized yet
            new_node.next = new_node  # loop created
        self.head = new_node  # updated head

    # print item in list        --O(n)
    def print_list(self):
        curr = self.head
        if self.head is not None:
            while True:
                print(curr.data, end=" -> ")
                curr = curr.next
                if curr is self.head:
                    print()
                    break
        else:
            print("No node in circular list.")


# Linked list class
class LinkedList(List):
    def __init__(self):
        self.head = None

    # push node to head         --O(1)
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # print element in list     --O(n)
    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end="->")
            curr = curr.next
        print('None')


# Code execution begins here
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.print_list()

    for elem in [4, 3, 2, 1]:
        clist.push(elem)

    clist.print_list()
    print('Detect loop in circular list:', clist.detect_loop())

    llist = LinkedList()
    llist.print_list()

    # add element to list
    for elem in [10, 12, 23, 45]:
        llist.push(elem)

    llist.print_list()
    print('Detect loop in list:', llist.detect_loop())

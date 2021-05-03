# Sorted insert for circular Linked list
"""
- Allocate a node for new value say (new_node)

Algorithm:
Case 1: Linked List is empty :
    1. Create a self loop
        new_node.next = new_node
    2. Update head to new_node
        self.head = new_node
Case 2: New Node is to be inserted before the head node:
    1. Change next of new_node to prev head pointed node
        new_node.next = self.head
    2. Find the last node, and change its next to create loop.
        last.next = new_node
    3. Update head to new_node
        self.head = new_node
Case 3: To be inserted somewhere :
    1. Find a node after(say; before_node ) which this new_node is to be inserted
    2. Change next of new_node to before_node 's next
        new_node.next = before_node.next
    3. Link before_node and new_node
        before_node.next = new_node
"""


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:

    def __init__(self):
        self.head = None

    # push node to head of list
    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            # find last node update next
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            # we got last node pointed by temp ; create a loop
            temp.next = new_node

            # update next of new_node to prev head
            new_node.next = self.head
        else:
            # create a loop
            new_node.next = new_node

        # point new_node to be head node
        self.head = new_node

    # function for sorted insert of element in list
    def sorted_insert(self, value):

        curr = self.head
        new_node = Node(value)

        # case1 : list empty
        if curr is None:
            new_node.next = new_node        # loop created
            self.head = new_node            # updated head

        # case2 : New_node to be inserted before head
        elif value <= curr.data:
            new_node.next = curr        # change next of new_node to prev head

            # find last node and change its next to point new_node (create loop)
            while (curr.next is not self.head):
                curr = curr.next

            # we got last node pointed by curr
            curr.next = new_node

            # update head to point new_node
            self.head = new_node

        # case3 : New_node to be inserted somewhere else
        else:
            # locate node before which new_node is to be inserted
            while(curr.next is not self.head) and (curr.next.data < value):
                curr = curr.next

            # we got curr(node before new_node to be inserted)
            new_node.next = curr.next
            curr.next = new_node

    # print list            -- O(n)
    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp is self.head:
                    print()
                    break
        else:
            print("No node in list to display.")


# Code execution begins here
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.print_list()

    # add node
    for elem in [150,43,8,90,12,140]:
        clist.sorted_insert(elem)

    clist.print_list()
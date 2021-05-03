# Insertion of nodes in Singly circular linked list


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class CircularList:

    def __init__(self):
        self.last = None

    # insertion in an empty list
    def add_to_empty(self, value):
        if self.last is None:
            self.last = Node(value)
            self.last.next = self.last  # create loop
        else:
            self.add_to_begin(value)

    # insertion at beginning of list
    """
    2 -> 1 -> 2        (Initial)
         |
        last  
    Add 3:
        3.next = 1.next = 2
        1.next = 3
    3 -> 2 -> 1 -> 3       (Final)
              |
            last  
    """

    def add_to_begin(self, value):

        if self.last is not None:
            # create new Node object
            new_node = Node(value)

            new_node.next = self.last.next
            self.last.next = new_node
        else:
            self.add_to_empty()

    # insertion at end of list
    """
    1 -> 2 -> 3 -> 1 
              |
             last
    Add 4 to end :
    new_last.next = last.next           # 4.next = 1
    last.next = new_last                # 3.next = 4
    self.last = new_last                # last = 4
    
    1 -> 2 -> 3 -> 4 -> 1 
                   |
                 last
    """

    def add_to_end(self, value):
        if self.last is not None:
            # new last node
            new_last = Node(value)
            new_last.next = self.last.next
            self.last.next = new_last
            self.last = new_last

    # insertion in between of list
    """
    1 -> 2 -> 3 -> 1
              |
             last
    Add 55 after 2:
    * Steps:
    1. Create a new_node say T
    2. Search for node after which T is to be inserted, say it P
    3. T.next = P.next
    4. P.next = T
    """

    def add_after(self, value, node_val):

        if self.last is None:
            return None

        new_node = Node(value)
        # begin search for node with value
        temp = self.last.next  # first node
        while temp.data != node_val:
            if temp is self.last:
                print("No such element ,%d" % node_val)
                return None
            temp = temp.next

        # elem with value is found
        if temp.data == node_val:
            new_node.next = temp.next
            temp.next = new_node

            # test if temp was last node itself
            if temp is self.last:
                self.last = new_node


    # display circular linked list
    """
    1. temp -> last.next
    2. traverse from last to all next node, updating temp, until temp is last
    """

    def display(self):
        if self.last:
            temp = self.last.next
            while temp is not self.last:
                print(temp.data, end=' -> ')
                temp = temp.next

            # to show loop
            print(self.last.data)
        else:
            print('No element to display')



# Code begins here

if __name__ == "__main__":
    # initialize circular linked list
    clist = CircularList()

    clist.display()

    # add elements
    clist.add_to_empty(1)
    clist.add_to_begin(2)
    clist.add_to_empty(3)

    clist.display()

    # add to end
    clist.add_to_end(40)
    clist.add_to_end(50)

    clist.display()

    # add after 2
    clist.add_after(-12, 2)
    clist.display()

    # add after 3
    clist.add_after(-13, 3)
    clist.display()

    # add after 50
    clist.add_after(-9, clist.last.data)
    clist.display()

    # add after not in list number
    clist.add_after(-7, 437)
    clist.display()

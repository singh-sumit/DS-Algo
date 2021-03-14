'''
Insertion on list can be done in :
    1. At head of list
    2. In between Node
    3. At end of list
'''

# Node class
class Node:

    # function to initialize node object
    def __init__(self, data):
        self.data = data        # Assigning provided data
        self.next = None        # Initialize next pointer of each node to None
    
# Linked List class
class LinkedList:

    # function to initialize the linked list object
    def __init__(self):
        self.head = None

    
    # function print/traverse node in list
    def display(self):
        curr = self.head
        print('HEAD -> ',end='')

        # Traverse till curr node is not None
        while curr is not None:
            print(f'{curr.data}',end=' -> ')
            curr = curr.next            # update curr to next of this node
        
        print('None')

    # function to add node to head of linked list
    def add_to_head(self, data):
        '''
            1. Create a node object with given data
            2. Refer newNode next to previous head's next
            3. Make newNode to be head pointed node
        '''
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    

    # function to add node to end of linked list
    def add_to_end(self, data):
        '''
        1. Create a node object with given data
        2. Find last node
            i. Traverse till end of list
        3. Mark last node next to refer newNode
        '''
        newNode = Node(data)

        curr = self.head
        prev = None         # to keep record of node with next is None
        while curr is not None :
            prev = curr
            curr = curr.next

        # if still prev is None; then it means list has no element yet
        if prev is None:
            self.head = newNode
        else:
            prev.next = newNode


    # function to add node in between two nodes in linked list
    # Inserts a new node after given prev_node
    def add_in_between(self, data, prev_node_data):

        '''
        1. Search for node with prev_node_data 
            If don't exist return 'Message'
            Else 
                i. Create a node object with given data
                ii. make newNode next ot refer prev_node next
                iii. make prev_node next to refer newNode
        '''

        curr = self.head
        while (curr is not None) and (curr.data != prev_node_data):
            curr = curr.next        # update curr to move forward
        
        # at this point curr holds data with prev_node_data or is None
        if curr is None:
            print("Given prev node data is not present.")
            return 
        else:
            newNode  = Node(data)
            newNode.next = curr.next
            curr.next = newNode    


# Code execution begins here
if __name__ == "__main__":

    # Initialize empty linked list
    llist = LinkedList()

    llist.display()

    # inserting at head of list
    llist.add_to_head(3)
    llist.add_to_head(2)
    llist.add_to_head(1)

    llist.display()

    # inseting at end of list
    llist.add_to_end(4)
    llist.add_to_end(5)
    llist.add_to_end(6)

    llist.display()

    # inserting after certain node
    llist.add_in_between(10,3)
    llist.add_in_between(22, 1)

    llist.add_in_between(55, -9)

    llist.display()
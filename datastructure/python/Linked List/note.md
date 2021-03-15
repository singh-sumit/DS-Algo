# Linked List

- Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

- ![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)

## Why Linked List :
Arrays can be used to store linear data of similar types, but arrays have the following limitations.

1. Size of arrays is fixed.
2. Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

For example, in a system, if we maintain a sorted list of IDs in an array id[].

id[] = [1000, 1010, 1050, 2000, 2040].

And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000).
Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved.

## Advantages over arrays :
1) Dynamic size
2) Ease of insertion/deletion

## Drawbacks of Linked list:
1) **Random access is not allowed**. We have to access elements sequentially starting from the first node. So *we cannot do binary search with linked lists efficiently* with its default implementation. 
2) **Extra memory space for a pointer is required** with each element of the list.
3) **Not cache friendly**. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

## Representation:
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node

```python
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
```

## Implementation :
```python
# A simple Python program for traversal of a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
  
  
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node 
  
    llist.printList() 
```


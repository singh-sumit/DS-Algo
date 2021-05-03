# Circular Linked List :
---

## Introduction:

- linked list where all nodes are connected to form a circle.
- No NULL at the end of list
- can be *singly* or *doubly* circular linked list

![image](https://media.geeksforgeeks.org/wp-content/uploads/CircularLinkeList.png)

## Advantage:

- Any node can be starting point. i.e; we need to start and find the same node to stop.
- Useful for queue implementation; don't need to maintain two **front** and **rear** pointer.
- Useful for tasks,that needs for repeatedly going the list.

## Implementation :

![image](https://media.geeksforgeeks.org/wp-content/uploads/CircularSinglyLinkedList1.png)
- As last node points to first node; **it is good keep tracking last Node.**
- Why, 
    - As for **insertion** :
    
    i.e at the head of list(before P); **operation is O(1)**
    ```
    newNode.next = last.next
    last.next = newNode
    ```
### Insertion:

1. Insertion in empty list
2. Insertion at begin
3. Insertion at end
4. Insertion after node   -O(n)

## Traversal:

1.
```python
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
```



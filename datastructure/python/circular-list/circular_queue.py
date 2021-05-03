# Circular Queue is linear datastructure , operates on FIFO principle,
# last position is connected back to the first position to make a circle.
"""
In normal queue, we can insert elements until queue is full.
But once queue is full, we cannot insert next element, if there is a space in front of queue.
"""

"""
Operations on Cicular Queue:
1. Front:   Gets front item form the queue.
2. Rear:    Gets last(recent inserted) item from the queue.
3. enQueue(value) :
    - Used to insert a element to (rear position) of the circular queue.
    1. Check whether a queue is full.
    2. If it is full then display Queue is FULL.
        If queue is NOT FULL, check if (rear != SIZE-1 && rear != front-1); is TRUE,
        then set rear=0; and insert element.
4. deQueue():
    - func, used to delete an element from the circular queue.
    - elem, always deleted from front position.
    1. Check whether queue is EMPTY(check if (front==-1))
    2. If queue is empty, then display QUEUE is EMPTY. 
    3. Else,
        -         
"""
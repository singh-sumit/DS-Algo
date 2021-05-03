# count nodes in a circular list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# circular list
class CircularLinkedList:

    def __init__(self):
        self.head = None

    # push node to head of list         --O(1)
    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            # find the last node of list and update its next to new_node
            last = self.head
            while (last.next is not self.head):
                last = last.next  # traverse to next node
            # we got last node
            last.next = new_node

            # link new_node to prev head node
            new_node.next = self.head
        else:
            # list is not initialize yet
            new_node.next = new_node  # creating a self loop

        self.head = new_node  # update a head node of list

    # function to count the nodes in list       --O(n)
    def count(self):
        curr = self.head
        count = 0
        if self.head is not None:
            while True:
                curr = curr.next        # update to move forward
                count += 1
                if curr is self.head:
                    break
        return count

    # function to display nodes in list         --O(n)
    def print_list(self):
        curr = self.head
        if curr is not None:
            while True:
                print(curr.data, end=" -> ")
                curr = curr.next
                if curr is self.head:
                    print()
                    break
        else:
            print("No node in list")


# Code execution begins here
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.print_list()

    # adding item to list
    for elem in [4, 5, 7, 8, 3]:
        clist.push(elem)

    clist.print_list()
    print("count :", clist.count())

# Linked List
	# is list of nodes in linear fashion, each nodes refering to next of itself.
	# Each Node has data, and next pointer
	# Linked list class has a head pointer


# Node class
class Node:

	# Function to initialize the node object
	def __init__(self, data):
		self.data = data	# Assign data
		self.next = None 	# Initialize next as null


# Linked List class
class LinkedList:

	# Function to initialize the Linked list object
	def __init__(self):
		self.head = None

	# Function to traverse in list
	'''
		Keeping traversing until node's next is None
	'''
	def print(self):
		curr = self.head
		print('HEAD -> ',end='')
		while(curr is not None):
			print(curr.data,end=' -> ')
			curr = curr.next #update curr node
		print('None')



# Code execution starts here
if __name__ == '__main__':

	# Start with empty Linked List
	llist = LinkedList()

	# Adding Node
	# head -> 1 -> 2-> 3-> 4
	llist.head = Node(1)
	
	# Three nodes
	second = Node(2)
	third = Node(3)
	fourth = Node(4)

	# Now joining Each node using next pointer
	llist.head.next = second
	second.next = third
	third.next = fourth

	# Traverse in linked list
	llist.print()

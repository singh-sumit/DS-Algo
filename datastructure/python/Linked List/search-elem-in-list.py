"""Problem : Find the element with in linked list
Iterative Solution :
	1. Traverse and search for element 
	2. If curr is None , ELEMENT NOT FOUND
	3. Else ,Found
Recursive Solution:
	1. 
"""

# Node class 
class Node:

	# function to initialize instance member of Node class
	def __init__(self, data):
		self.data = data
		self.next = None

# Linked list class
class LinkedList:

	# function to initialize instance member of Linkedlist class
	def __init__(self):
		self.head = None
	
	# function to push node to linked list		-O(1)
	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	# function to display/ traverse linked list 	-O(n)
	def display(self, curr):
		# base condition
		if curr is None:
			return 'None'

		return str(curr.data)+' -> '+self.display(curr.next)

	
	# function to search an element in list
	# Iterative Way					- O(n)
	def iter_search(self, key):
		curr = self.head
		while(curr is not None):
			if curr.data == key:
				return True

			curr = curr.next

		return False
	
	# function to search an element in list
	# Recursive Way							- O(n)
	def recur_search(self, curr, key):

		# base condition
		if curr is None:
			return False
		elif curr.data == key:
			return True
		
		return self.recur_search(curr.next , key)



# Code execution Begins here
if __name__ == "__main__":

	# Initialize Linked list
	llist = LinkedList()

	print(llist.display(llist.head))

	# push node item
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)

	print(llist.display(llist.head))


	# Search 
	print('Iter_Search for item ',4,llist.iter_search(4))
	print('Recur_Search for item ',4,llist.recur_search(llist.head,4))

	print('Iter_Search for item ',1,llist.iter_search(1))
	print('Recur_Search for item ',1,llist.recur_search(llist.head,1))
	
	print('Iter_Search for item ',5,llist.iter_search(5))
	print('Recur_Search for item ',5,llist.recur_search(llist.head,5))
	
	print('Iter_Search for item ',-10,llist.iter_search(-10))
	print('Recur_Search for item ',-10,llist.recur_search(llist.head,-10))

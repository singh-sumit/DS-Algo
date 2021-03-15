'''
Deleting a node given a key:
1. Find prev_node of node to be deleted
2. Change next of prev_node to next of deletable_node
3. Free up memory for the deletable_node
'''

# Node class
class Node:

	def __init__(self, data):
		# function to initialize node object with given data
		self.data = data		
		self.next = None 
	

# Linked List Class
class LinkedList:

	def __init__(self):
		# function to initialize linked list object
		self.head = None
	
	# Node addition 	-O(1)
	def push(self, data):
		'''function to add node to head of list
		'''

		'''
		1. Create a new node object with given data
		2. Change next of newNode to refer head
		3. Make newNode to be refered by head
		'''

		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	# Node deletion 
	def delete(self, del_data):
		# function to delete data from linked list

		'''
		1. Find the node prev to del_data_node
		2. Make prev_node next to refer next of del_node
		3. Free up memmory for del_node
		'''

		# if first node itself is del_node
		if (self.head is not None) and (self.head.data == del_data):
			self.head = self.head.next
			print(f'{del_data} ,Deleted successfully.')
			return 

		# Search for del_node through list
		curr = self.head
		prev = None
		
		# keep moving until curr refer to prev to del_node
		while (curr is not None) and (curr.data != del_data):
			prev = curr
			curr = curr.next			# update curr to move forward

		# At this point either del_node is found or not found
			# If curr points to None then del_node is NOT FOUND.
			# Else 			del_node is FOUND,prev point to some node
		if curr is None:
			print(f'NODE with {del_data} NOT FOUND!!')
			return 
		else:
			prev.next = prev.next.next
			print(f'{del_data} ,Deleted successfully.')
	
	# function to display/traverse node in list
	def display(self):
		'''
		1. Make curr to refer head node
		2. Traverse and print until curr refer None
		'''
		curr = self.head

		print('HEAD',end='->')

		while curr is not None:
			print(curr.data,end=' -> ')
			curr = curr.next		# update curr to move forward
		
		print('None')


# Code Execution Begins Here
if __name__ == "__main__":

	# initialize empty linked list
	llist = LinkedList()

	llist.display()

	# Node addition
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)


	llist.display()

	# Deletion
	llist.delete(2)

	llist.display()

	llist.delete(1)
	llist.display()

	llist.delete(5)
	llist.display()


	llist.delete(11)
	llist.display()
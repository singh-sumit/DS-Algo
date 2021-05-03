"""Problem: Given an index, get an node at that index from end of list
Solution:
	a. ITERATIVE SOLUTION:
		1. Calculate diff = len-index+1
		2. Traverse node from begining until diff = 0
	b. RECURSIVE SOLUTION:

	c. Using Two Pointer Method(Confusion):link(https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/):
		1. First Initialize two pointers main, and ref_pointer to head of list
		2. Initialize count =0 , and index is given(from the end of list)
		3. Traverse the list until count==index given and update ref_pointer
		4. Move ref_pointer and main_pointer one by one until ref_pointer points to None
			i. At this point main_pointer holds the required node
"""

# Node class
class Node:

	# function to initialize node object
	def __init__(self, data):
		self.data = data
		self.next = None

# Linked List class
class LinkedList:

	# function to initialize LinkedList object
	def __init__(self):
		self.head = None
	
	# function to push node to head of linked list 
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# function to display/ traverse node in linked list
	def display(self, curr):

		# Base Condition
		if curr is None:
			return 'None'
		return str(curr.data) + ' -> '+self.display(curr.next)

	# function to get nth node from end of list ITERATIVE SOLUTION
	def iter_get_nth_from_end(self, index):

		# calculate total length of linked list
		len = 0
		curr = self.head
		while(curr is not None):
			len +=1
			curr = curr.next
		
		# calculate diff b/w index to cover from beginning
		diff = len-index

		# if diff is negative return index is too High or if diff is greater than len return too small
		if diff<0:
			print(f'Index :{index} too High!! Select b/w 1 - {len}')
			return
		elif diff>=len:
			print(f'Index :{index}  too Small!! Select b/w 1 - {len}')
			return
		else:
			# is in range
			# traverse node till diff is not zero
			curr = self.head
			# while diff != 0:
			# 	curr = curr.next
			# 	diff -=1

			for i in range(0, diff):
				curr = curr.next
			'''if index =2 , len =5 ,	difff = 4, to obtain =node4
			
			 diff = 4 			curr = head/node1 			after_diff = 3
					3					node2							2
					2					node3							1
					1					node4							0
			'''
			print(f'Data at index :{index} is :{curr.data}')
			return

	# function to get nth node from end of list ITERATIVE SOLUTION
	def recur_get_nth_from_end(self, curr, index, counter=0):
		
		# base condition
		if curr is None:
			print(f'Index :{index} is not correct.')
			return
		elif index == counter:
			print(f'Node at index : {index}, is :{curr.data}')
			return
		# recursively call itself
		return self.recur_get_nth_from_end(curr.next, index, counter+1)

	# function to get node from the end of list using Two-pointer method
		"""
		1. First Initialize two pointers main, and ref_pointer to head of list
		2. Initialize count =0 , and index is given(from the end of list)
		3. Traverse the list until count==index given and update ref_pointer
		4. Move ref_pointer and main_pointer one by one until ref_pointer points to None
			i. At this point main_pointer holds the required node
		"""
	def get_nth_node_from_end(self, index):
		# initialize two pointers and counter
		main_pointer = self.head
		ref_pointer = self.head
		count = 0

		if self.head is not None:

			# Traverse ref_pointer
			while count < index:
				if ref_pointer is None:
					print(f"Index : {index}, you entered is too large.")
					return
				ref_pointer = ref_pointer.next
				count +=1
			
			# check if ref_pointer already reached None
			if ref_pointer is self.head:
				print(f'Provide index :{index} is too small.')
			else:
				# traverse main and ref_pointer one by one until ref_pointer is not None
				while (ref_pointer is not None):
					main_pointer = main_pointer.next
					ref_pointer = ref_pointer.next
			
				# now main_pointer refers to node at that index from end of list
				print(f"Node at index : {index} is {main_pointer.data}")
				return 

# Driver Code
if __name__ == "__main__":

	# initialize empty linked list
	llist = LinkedList()

	print(llist.display(llist.head))

	# push node
	llist.push(50)
	llist.push(40)
	llist.push(30)
	llist.push(20)
	llist.push(10)

	print(llist.display(llist.head))

	# find nth node from end of linked list
	llist.iter_get_nth_from_end(5)		# 10
	llist.iter_get_nth_from_end(4)		# 20
	llist.iter_get_nth_from_end(3)		# 30
	llist.iter_get_nth_from_end(1)		# 50

	llist.iter_get_nth_from_end(6)		
	llist.iter_get_nth_from_end(0)		
	llist.iter_get_nth_from_end(-1)		


	# using recursive function
	print('Recursively')
	llist.recur_get_nth_from_end(llist.head, 5-1)			# 50
	llist.recur_get_nth_from_end(llist.head, 5-2)			# 40
	llist.recur_get_nth_from_end(llist.head, 5-5)			# 10
	llist.recur_get_nth_from_end(llist.head, 5-4)			# 20

	llist.recur_get_nth_from_end(llist.head, 5-(-1))		
	llist.recur_get_nth_from_end(llist.head, 5-0)			
	llist.recur_get_nth_from_end(llist.head, 5-6)			


	# using two pointer method
	print("Using Two pointer method")
	print(llist.display(llist.head))
	llist.get_nth_node_from_end(2)
	llist.get_nth_node_from_end(1)
	llist.get_nth_node_from_end(5)
	llist.get_nth_node_from_end(4)
	llist.get_nth_node_from_end(0)
	llist.get_nth_node_from_end(6)
	llist.get_nth_node_from_end(-2)
	

"""Problem: Given a linked list detect, list contains loop or not.
Solution:
	a. Using a variable and Storing first node.(Iterative approach)
	b. Using hashset(Storing all visited nodes)
	c. Modifying basic linked list to be have another fields(visited_flag); and mark each visited_flag
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
	
# Linked list class
class LinkedList:

	def __init__(self):
		self.head =  None
	
	# method to push node to head of list		--O(1)
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		return self.head
	
	# method to display nodes in linked list		--O(n)
	def display(self):
		curr = self.head
		print('HEAD', end=' -> ')
		while(curr is not None):
			print(curr.data, end=' -> ')
			curr = curr.next
			
			# break if loop present
			if (curr is self.head):
				break

		print('None')
	
	# function to detect loop USING ITERATIVE approach
	# Time complexity 		-- O(n)
	# Auxiliary Space 		--O(1)
	def is_loop_present(self):
		"""Steps:
		1. Set first -> self.head element
		2. Iterate over the list until last Node
		3. Check if last_node == first	; Then RETURN True
				else					; 	   RETURN False
		"""
		if self.head:
			first =  self.head
			curr = self.head		# curr holds last node
			while curr.next is not None:
				curr = curr.next

				# check for loop\
				if (curr is first):
					return True
			
			# check if firt and last node are same
			return False
		else:
			print('List is empty')

	# method to detect loop using hashset(storing all visited nodes & comparing with un_visited nodes)
	def check_for_loop(self):
		if self.head:		# if list is not empty
			visited = set()
			curr = self.head
			while (curr):			# until curr is not None
				# if curr node is visited then LOOP DETECTED
				if(curr in visited):
					return True
				
				# else include curr to set
				visited.add(curr)

				# update curr to move forward
				curr = curr.next
			
			# if while loop completes without satisfying inner if condition
			return False
		else:
			print('List empty')


# Code execution begins here
if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	llist.display()

	# push node to linked list 
	last = llist.push(5)
	for n in [4,3,2,1]:
		llist.push(n)
	
	# create loop
	last.next = llist.head

	llist.display()

	#
	print('Loop present ?', llist.is_loop_present())
	print('Loop present ?', llist.check_for_loop())
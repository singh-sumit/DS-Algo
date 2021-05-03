""" Approach : Modifying basic linked list structure to include another visited_flag
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.visited_flag = 0
	
# LinkedList class
class LinkedList:

	def __init__(self):
		self.head = None
	
	# method to push node to linked list 		--O(1)
	def push(self, data):
		new_node =  Node(data)
		new_node.next =  self.head
		self.head = new_node
		
		return self.head

	# method to display loop presented linked list		--O(n)
	def display(self):
		curr = self.head
		print('HEAD', end=' -> ')
		while(curr is not None):
			print(curr.data , end=' -> ')
			curr = curr.next 		# update curr to move forward

			# check for loop if present break out
			if (curr is self.head):
				break
		
		print('NONE')

	
	# method to check for loop present in list			--O(n)
	def check_loop(self, curr):
		# Traverse the list and mark each unvisited node flag=1 ; and check for already visited one
		while(curr is not None):
			# if already visited
			if (curr.visited_flag == 1):
				return True
			
			# else curr node is new to be visited so mark flag
			curr.visited_flag = 1

			# update curr to move forward
			curr = curr.next

		# either the list is empty or has no loop in it
		print('Either list is empty or Has no loop')
		return False


# Code execution begins here
if __name__ == "__main__":

	# initialize linked list
	llist =  LinkedList()

	llist.display()

	# push node
	last = llist.push(5)

	for n in [4,3,2,1]:
		llist.push(n)
	
	# create loop for testing 
	last.next =  llist.head

	# displaying 
	llist.display()

	# checking
	print('Loop present ?', llist.check_loop(llist.head))

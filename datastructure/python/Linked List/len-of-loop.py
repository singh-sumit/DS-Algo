"""Problem: Find the length of loop if present in linked list
Solution:
	a. Using Floyd's Cycle detection algorithm
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Linked list class
class LinkedList:

	def __init__(self):
		self.head = None
	

	# method to push a node to linked list		--O(1)
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		return self.head
	
	# method to display a node in linked list if loop is present		--O(n)
	def display(self):
		curr = self.head
		print('HEAD', end=' -> ')
		while(curr):
			print(curr.data, end=' -> ')
			curr = curr.next  		# move curr to forward

			if (curr is self.head):		# detected cycle
				return 
		
		print('NONE')

	# method to find length of loop
	"""Steps:
		1. Find the common point in loop by using Floydl's Cycle detection algorithm.
		2. Store the pointer in temp. variable & set counter =0
		3. Traverse linked list until same node is reached again; & increase counter on moving each node.
		4. Print count as length of loop.
	"""
	def get_count(self):

		# if list is empty; then list has NO LOOP return count->0
		if self.head is None:
			return 0
		
		# Detect loop (Using Floyd's Cycle Detection Algo.)
		slow = self.head
		fast = self.head

		while(fast and fast.next and fast.next.next):		# until fast, or fast.next, of fast.next.next is not None
			# move fast by two position
			fast = fast.next.next

			# check if fast==slow Then; CYCLE IS DETECTED
			if (fast == slow):
				# now count nodes from current node until travesing and getting same node
				temp = slow.next
				count = 1
				while(temp is not slow):
					temp = temp.next
					count += 1
				return count

			# else move slow by one position
			slow = slow.next

		# if controls comes here return 0 as list has no loop.
		return 0	


# Code execution Begins Here
if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	# display list
	llist.display()

	# push node
	last = llist.push(5)

	for n in [4,3,2,1]:
		llist.push(n)
	
	# create a loop
	last.next = llist.head

	# get count nodes in looped list
	print('Len of loop :',llist.get_count())
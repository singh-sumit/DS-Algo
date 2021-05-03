"""Problem: Count the number of times given int occurs
Solution:
	a. Using Auxiliary var(count) & by Iterating
	b. Using Auxiliary var(count) & by Recursion

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

	# method to push node to head of list		--O(1)
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	
	# method to print nodes in list 		--O(n)
	def display(self):
		curr = self.head
		print('HEAD', end=' -> ')
		while (curr is not None):
			print(curr.data, end=' -> ')
			curr = curr.next
		print('None')
	
	# method to count the occurence of given int	
	# Time Complexity -- O(n)
	# Auxiliary Space -- O(1)
	def get_occ(self, num):
		count = 0
		curr = self.head
		while(curr is not None):
			if curr.data == num:
				count += 1
			
			curr = curr.next	# update curr to move forward
		
		return count
	
	# method to count the occurence of given int	USING RECURSION
	# Time Complexity -- O(n)
	# Auxiliary Space -- O(1)
	def get_occ_recur(self, count, curr, num):
		# Base condition
		if curr is None:
			return count
		elif curr.data == num:
			return self.get_occ_recur(count+1, curr.next, num)
		else:
			return self.get_occ_recur(count, curr.next, num)


# Code execution begins from here
if __name__ == "__main__":

	# initialize empty linked list
	llist = LinkedList()

	llist.display()

	# push nodes
	for n in [1,5,6,4,2,1,5,1,2,1,1,2]:
		llist.push(n)

	llist.display()

	
	print('Using Iterative method :')
	print(f'Occurence of {1} => {llist.get_occ(1)}')
	print(f'Occurence of {2} => {llist.get_occ(2)}')
	print(f'Occurence of {5} => {llist.get_occ(5)}')
	print(f'Occurence of {6} => {llist.get_occ(6)}')
	print(f'Occurence of {7} => {llist.get_occ(7)}')
	
	print('Using Recursive method :')
	print(f'Occurence of {1} => {llist.get_occ_recur(0, llist.head, 1)}')
	print(f'Occurence of {2} => {llist.get_occ_recur(0, llist.head, 2)}')
	print(f'Occurence of {5} => {llist.get_occ_recur(0, llist.head, 5)}')
	print(f'Occurence of {6} => {llist.get_occ_recur(0, llist.head, 6)}')
	print(f'Occurence of {7} => {llist.get_occ_recur(0, llist.head, 7)}')

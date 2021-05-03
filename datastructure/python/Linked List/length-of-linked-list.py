"""Problem : Find the length of linked list
Solution :
	1. Set count =0, curr = head
	2. Iterate over the linked list until curr is not None
	3. Increment count
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data

# Linked list class
class LinkedList:

	# instance member of linked list
	def __init__(self):
		self.head = None
	
	# function to push node to head of linked list
	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	# function to traverse the linked list
	def display(self, curr):
		# base condition
		if curr is None:
			# print()
			return 'None'
		 
		return str(curr.data)+'->'+self.display(curr.next)
	
	# function to find length of linked list RECURSIVE WAY
	def recur_size(self, curr, count :int)-> int:
		# base condition
		if curr is None:
			return count
			# pass
		
		return self.recur_size(curr.next, count+1)

	# function to find length of linked list ITERATIVE WAY
	def iter_size(self):
		curr = self.head
		count = 0
		while(curr is not None):
			curr = curr.next
			count +=1
		return count
# Code execution begins here

if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	print('Recursive size is :',llist.recur_size(llist.head, 0))
	print('Iterative size is :',llist.iter_size())
	# push node
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)

	print(llist.display(llist.head))

	print('Recursive size is :',llist.recur_size(llist.head, 0))
	print('Iterative size is :',llist.iter_size())


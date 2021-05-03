'''
Problem : Given a key to node delete a first occurence of node in linked list using Recursive way
Solution :
	1. Find the node prev_node to del_node in recursive way
	2. Change next of prev_node to prev_node.next.next(i.e, del_node.next)
'''

# Node class
class Node:

	# instance member of Node class
	def __init__(self, data):
		self.data = data
		self.next = next

# Linked List class
class LinkedList:

	# Instance member of LinkedList class
	def __init__(self):
		self.head = None
	
	# prit / Traverse Nodes in linked list
	def display(self):
		print('HEAD', end=' -> ')
		curr = self.head
		while curr is not None:
			print(curr.data, end=' -> ')
			curr = curr.next 			# update to move forward
		
		print('None')

	# push node to head of linked list
	def push(self, data):
		newNode = Node(data)

		newNode.next = self.head
		self.head = newNode
	
	# function to delete node in recursive manner
	def remove(self,curr, data):

		# if curr is None meaning Head is not initialize other wise we have moved to end
		# The element does not exits
		if curr is None:			# base condition
			print(f'Node with {data} Does not Exists.')
			return 
		
		# check for node with data if yes change prev.next to prev.next.next
		if curr.data == data or (curr.next is not None and curr.next.data == data):
			if curr == self.head:
				self.head = self.head.next
			else:
				curr.next = curr.next.next
			print(f'Node with {data} deleted successfully!')
			return
		
		# else recurse
		self.remove(curr.next , data)


# Code execution begins from here
if __name__=="__main__":

	# initialize linked list
	llist = LinkedList()

	llist.display()

	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)

	llist.display()


	# Deletion 
	llist.remove(llist.head, 3)
	llist.display()

	llist.remove(llist.head, 1)
	llist.display()

	llist.remove(llist.head, 5)
	llist.display()

	llist.remove(llist.head, 20)
	llist.display()

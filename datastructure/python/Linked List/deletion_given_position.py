"""Problem: Given a position Delete a node 
Solution :
	1. Find if position exists in size of linked list
	2. If yes, then change next pointer of this node to curr.next.next
	3. Else ,return position not in range
"""

# Node class
class Node:

	# instance variable of Node object
	def __init__(self, data):
		self.data = data
		self.next = next

# class Linked List
class LinkedList:

	# instance of linked list object
	def __init__(self):
		self.head = None
		self.size = 0
	
	# function to push node to head of linked list
	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode
		self.size +=1
	
	# function to display/ traverse node in linked list
	def display(self):
		
		print('HEAD', end='->')
		
		curr = self.head
		while curr is not None:
			print(curr.data, end='->')
			curr = curr.next		# update curr to move forward in list

		print('None')

	# function to delete node given a position
	def del_at(self, pos):
		if pos < 1 or pos > self.size:
			print(f'Position :{pos} , not in range.(0-{self.size})')
			return

		# else pos is in range
		#Travese node till before node in that pos
		tem_pos = pos
		curr = self.head			
		if pos != 1:
			pos -= 1
			while (pos != 1):
				curr = curr.next
				pos -=1		# decrement pos

			# Now curr points to node before then node in given pos
			del_node = curr.next
			curr.next = del_node.next
		else:				# first position element
			del_node = self.head
			self.head = curr.next
		print(f'Node with value {del_node.data}, at position : {tem_pos}, deleted Successfully.')
		self.size -= 1

	

# Code execution begins here:
if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	llist.display()

	# push node
	llist.push(55)
	llist.push(44)
	llist.push(33)
	llist.push(22)
	llist.push(11)

	llist.display()

	# deletion
	llist.del_at(2)
	llist.display()

	llist.del_at(5)

	llist.del_at(4)
	llist.display()


	llist.del_at(1)
	llist.display()


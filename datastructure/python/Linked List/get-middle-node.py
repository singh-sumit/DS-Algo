"""Problems: Get a middle node from a singly-linked list
Solution:
	a. Method-1:
		1. Count the total number of node in linked list (say,n)
		2. Traverse till (n/2) and get node at that position
	b. Method 2 (Using slow & fast pointer):
		1. Initialize slow,fast = head
		2. Move fast by 2 pos followed by slow by 1 pos. Until fast reach None
		3. When fast==None, slow is mid-node
	c. Method 3 (Using Counter):
		1. Initialize mid-> head of list,& curr-> head, Count =0
		2. Increment Count and move curr, Until curr is not None.
		2. For every ODD count move mid forward

		e.g:
		1 -> 2 -> 3 -> 4 -> 5			;count =0 , curr =1 is not NONE ; mid = 1; curr = 2; count =1
										;count =1 , curr =2 is not NONE ; mid = 2; curr = 3; count =2
										;count =2 , curr =3 is not NONE ; mid = 2; curr = 4; count =3
										;count =3 , curr =4 is not NONE ; mid = 3; curr = 5; count =4
										;count =4 , curr =5 is not NONE ; mid = 3; curr = NONE; count =5
										;count =5 , curr =NONE is  NONE ; EXISTS
						SO mid =3

											
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

# Linked List class
class LinkedList:

	def __init__(self):
		self.head = None
	
	# function to push node to head of linked list
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	
	# function to display/ traverse node in linked list
	def display(self, curr):
		# base condition
		if curr is None:
			return 'None'
		
		return str(curr.data)+' -> '+self.display(curr.next)
	
	# function to count node in linked list			--O(n)
	def size(self, curr):
		# base condition
		if curr is None:
			return 0
		
		return 1+self.size(curr.next)

	# function to get middle node on traversing till middle node 		--O(n/2)
	def get_mid_node(self):
		curr = self.head
		len = self.size(curr)
		# print('Len is ',len)
		mid_index = len//2
		for i in range(0,mid_index):
			curr = curr.next
		return curr
	
	# function to get middle node USING SLOW & FAST POINER		--O(n)
	def get_mid_node_two_pointer(self):
		slow = self.head
		fast = self.head

		while (fast is not None) and (fast.next is not None):
			fast = fast.next.next
			slow = slow.next

		return slow

	# function to get mid node using method-3
	def get_mid_node_odd_move(self):

		mid = self.head
		curr = self.head
		count = 0

		while curr is not None:

			# move mid only when count is odd
			if count&1 == 1: 		# meaning odd
				mid = mid.next
			
			# move curr
			curr = curr.next
			count += 1
		
		# at this point mid holds middle node or list is not initialized yet
		return mid

	
# Code execution begins here
if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	print(llist.display(llist.head))

	# push of node
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)

	print(llist.display(llist.head))

	print('Mid node :', llist.get_mid_node().data)

	print('Mid node :', llist.get_mid_node_two_pointer().data)

	print('Mid node :', llist.get_mid_node_odd_move().data)
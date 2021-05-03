""" Approach : Floyd's Cycle Finding Algorithm
	Using slow and fast pointer
"""

# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
	
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
	def check_loop(self):
		"""
			1. Set slow=fast = head of list
			2. Move fast by two position if fast.next.next != None &
			3. Check for cycle(if slow == fast)
			4. If not ; move slow by one position
		"""
		"""
				1 -> 2 -> 3 -> 4 -> 1
				^
				|
			slw,fst
				1 -> 2 -> 3 -> 4 -> 1
					^	  ^
					|	  |
					slw	 fst
				1 -> 2 -> 3 -> 4 -> 1
						^           ^
						|           |
						slw        fst
				1 -> 2 -> 3 -> 4 -> 1
						^         
						|         
					fst,slw      --> Loop Detected
		"""
		slow = self.head
		fast = self.head
		while((fast) and (fast.next is not None) and (fast.next.next is not None)):
			fast =  fast.next.next 			# move fast by two position
			if(fast is slow):			# detected a cycle
				return True
			
			# else no cycle is detected ; Move slow by one position
			slow = slow.next
		# if control comes here ; either loop doesnot exist, or list is empty
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
	print('Loop present ?', llist.check_loop())

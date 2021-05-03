"""Problem : Given a position, return node at that position
Solution :
	a. Iterative Solution:
		1. Initialize count =  0
		2. Traverse through list unitl count == index
		3. Return index 
		4. If list ended, Return NOT FOUND
	b. RECURSIVE SOLUTION:
		1. Set function with parameter curr, count, index
		2. Base condition :if count == index		-> Retun curr
		3. 				elif curr has reached None 		-> Return NOT FOUND
		4. Else Recursively call function itself, with parameter curr.next, count+1, index
"""

# Node class
class Node:

	# function to initialize Node object
	def __init__(self, data):
		self.data = data
	
# Linked List Class
class LinkedList:

	# function to initialize LinkedList object
	def __init__(self):
		self.head = None
		
	# function to push node to linked list
	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	# function to display/ traverse node in linked list
	def display(self, curr):
		# Base condition
		if curr is None:
			return "None"
		return str(curr.data)+' -> '+self.display(curr.next)
	
	# function to get node at index ITERATIVE METHOD			-- O(n)
	def iter_get_at(self, index):
		# index is 0- based
		count = 0
		curr = self.head
		while curr is not None:
			if count == index:
				# At this point curr points node
				print('Node at index :',index,' is :',curr.data)
				return 
			
			curr = curr.next			# update curr node
			count +=1
		
		# if curr reached to last node it means node not found
		print('Node NOT FOUND for index, ',index)
		return -1
	
	# function to get node at index RECURSIVE METHOD 		--O(n)
	def recur_get_at(self, curr, count, index):
		# index is 0- based
		# Base condition
		if curr is None:
			print(f'NODE NOT FOUND, at index:{index}')
			return 
		elif count == index:
			print(f'Node :{curr.data} found for index {index}')
			return
		
		# recursively call function
		return self.recur_get_at(curr.next, count+1, index)



# Code Begins Here
if __name__ == "__main__":

	# initialize linked list
	llist = LinkedList()

	print(llist.display(llist.head))

	# push node
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)

	print(llist.display(llist.head))

	# find node at index
	print('Itetative way :')
	llist.iter_get_at(0)
	llist.iter_get_at(4)
	llist.iter_get_at(2)
	llist.iter_get_at(5)
	llist.iter_get_at(-1)

	print('REcursibe way :')
	llist.recur_get_at(llist.head, 0, 0)
	llist.recur_get_at(llist.head, 0, 4)
	llist.recur_get_at(llist.head, 0, 2)
	llist.recur_get_at(llist.head, 0, 5)
	llist.recur_get_at(llist.head, 0, -1)
	

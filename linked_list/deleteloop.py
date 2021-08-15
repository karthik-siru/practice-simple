# A Linked List Node
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


# Utility function to print a linked list
def printList(head):
	curr = head
	while curr:
		print(curr.data, end=" —> ")
		curr = curr.next
	print("None")


# Function to remove a cycle from a linked list pointed by `head` pointer.
# The `slow` pointer points to one of the nodes involved in the cycle
def removeCycle(slow, head):

	# Find the count of nodes involved in the loop
	k = 1
	ptr = slow
	while ptr.next is not slow:
		k += 1
		ptr = ptr.next

	# Get a pointer to k'th node from the head
	curr = head
	for _ in range(k):
		curr = curr.next

	# Simultaneously move the `head` and `curr` pointers at the same speed
	# until they meet. Also, maintain a previous pointer `prev` to `curr`

	prev = None
	while curr is not head:
		prev = curr
		curr = curr.next
		head = head.next

	# `curr` now points to the first node of the loop, and
	# `prev` points to the last node of the loop

	# set the next pointer of the previous node to None to break the chain
	prev.next = None


# Function to identify a cycle in a linked list using
# Floyd’s cycle detection algorithm
def identifyCycle(head):

	# take two pointers – `slow` and `fast`
	slow = fast = head

	while fast and fast.next:
		# move slow by one pointer
		slow = slow.next

		# move fast by two pointers
		fast = fast.next.next

		# if they meet any node, the linked list contains a cycle
		if slow == fast:
			return slow

	# we reach here if the slow and fast pointer does not meet
	return None


if __name__ == '__main__':

	# total number of nodes in the linked list
	n = 5

	# construct a linked list
	head = None
	for i in reversed(range(1, n + 2)):
		head = Node(i, head)

	# insert cycle
	head.next.next.next.next.next = head.next

	# first check if a cycle is present in a linked list
	slow = identifyCycle(head)

	# if a cycle is found, remove it
	if slow:
		removeCycle(slow, head)
		printList(head)
	else:
		print("No Cycle Found")
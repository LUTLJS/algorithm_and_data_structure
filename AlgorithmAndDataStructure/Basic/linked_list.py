#单向链表
#节点的实现
class SingleNode(object):

	def __init__(self, item):
		self.item = item
		self.next = None

#单链表的实现
class SingleLinkedList(object):

	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0

		while cur != None:
			count += 1
			cur = cur.next

		return count

	def travel(self):
		cur = self._head

		while cur != None:
			print cur.item
			cur = cur.next

	def add(self, item):
		#创建一个保存item值的节点
		node = SingleNode(item)
		#将新节点的链接域指向头节点
		node.next = self._head
		"""_head相当于q变量，让_head变量指向新节点"""
		self._head = node

	def append(self, item):
		node = SingleNode(item)

		if self.is_empty():
			self._head = node 

		else:
			cur = self._head

			while cur.next != None:
				cur = cur.next

			cur.next = node 
"""从头遍历到要插入的位置，将新节点的链接域
指向插入位置的下一个节点，将。。。找到位置，然后
打断这条链，强行把新节点插入（把位置的前一个节点
的链接域指向新节点，新节点的链接域指向下一个节点的
元素域)"""
	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			node = SingleNode(item)
			count = 0
			pre = self._head

			while count < (pos-1):
				count += 1
				pre = pre.next

			node.next = pre.next
			pre.next = node

	def remove(self, item):
		cur = self._head
		pre = None

		while cur != None:
			if cur.item == item:
				"""如果头节点为目标节点，则将头指针
				指向头节点的下一个节点"""
				if not pre:
					"""_head是头指针，cur和pre是两个
					节点"""
					self._head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def search(self, item):
		if self.is_empty():
			return
		 cur = self._head
		 while cur != None:
		 	if cur.item == item:
		 		"""print cur.item
		 		break"""
		 		return True
		 	cur = cur.next
		 return False


"""单向循环链表"""
class Node(object):
	def __init__(self, item):
		self.item = item
		self.next = None


class SinCycLinkedList(object):

	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head == None

	def length(self):
		if is_empty():
			return 0
		cur = self._head
		count = 0
		if cur.next == self._head:
			return 1
		else:
			while cur != self._head:
				count += 1
				cur = cur.next
			return count

	def length(self):
		if is_empty():
			return 0
		cur = self._head
		count = 1

		while cur.next != self._head:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		if self.is_empty():
			return
		cur = self._head
		print cur.item
		while cur.next != self._head:
			cur = cur.next
			print cur.item

	def add(self, item):
		node = SingleNode(item)
		
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			node.next = self._head
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			cur.next = node
			self._head = node

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			cur.next = node
			node.next = self._head

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			while count < (pos-1):
				count += 1
				cur = cur.next
			node.next = cur.next
			cur.next = node

	def remove(self, item):
		if self.is_empty():
			return
		cur = self._head
		pre = None
		if cur.item == item:
			if cur.next != self._head:
				while cur.next != self._head:
					cur = cur.next
				cur.next = self._head.next
				self._head = self._head.next
			else:
				self._head = None
		else:
			pre = self._head
			while cur.next != self._head:
				if cur.item ==item:
					pre.next = cur.next
					return
				else:
					pre = cur
					cur = cur.next
			if cur.item == item:
				pre.next = cur.next

	def search(self, item):
		if self.is_empty():
			return False
		cur = self._head
		if cur.item == item:
			return True
		while cur.next != self._head:
			cur = cur.next
			if cur.item == item:
				return True
		return False

"""双向链表"""
class Node(object):
	def __init__(self, item):
		self._head = item
		self.next = None
		self,prev = None


class DLinkList(object):
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		cur = self._head
		while cur != None:
			print cur.item
			cur = cur.next

	def add(self, item):
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			node.next = self._head
			self._head.prev = node
			self._head = node

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def search(self, item):
		cur = self._head
		while cur != None:
			if cur.item == item:
				return True
			cur = cur.next
		return False

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length(item)-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			while count < (pos-1):
				count += 1
				cur = cur.next
			node.prev = cur
			node.next = cur.next
			cur.next.prev = node
			cur.next = node

	def remove(self, item):
		if self.is_empty():
			return
		else:
			cur = self._head
			if cur.item == item:
				if cur.next == None:
					self._head None
				else:
					cur.next.prev = None
					self._head = cur.next
				return
			while cur != None:
				if cur.item == item:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
					break
				cur = cur.next













			










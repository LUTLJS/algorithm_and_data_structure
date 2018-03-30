"""Last in First out"""
class Stack(object):
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		"""弹出元素"""
		return self.items.pop()

	def peak(self):
		"""返回栈顶元素"""
		return self.items[len(self.items)]

	def size(self):
		"""返回堆栈的大小"""
		return len(self.items)

		


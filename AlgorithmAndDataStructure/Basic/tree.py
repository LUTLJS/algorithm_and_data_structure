class Node(object):

	 def __init__(self, elem=-1, lchild=None, rchirld=None):
	 	self.elem = elem
	 	self.lchild = lchild
	 	self.rchirld = rchirld


class Tree(object):
	
	def __init__(self, root=None):
		self.root = root

	def add(self, elem):
		node = Node(elem)
		if self.root == None:
			self.root = node
		else:
			queue = []
			queue.append(self.root)
			"""cur = queue.pop(0)
			对已有的节点进行遍历"""
			while queue:
				cur = queue.pop(0)
				if cur.lchild == None:
					cur.lchild = node
					return
				elif cur.rchirld == None:
					cur.rchirld = node
					return
				else:
					queue.append(cur.lchild)
					queue.append(cur.rchirld)


"""Depth First Search"""
def preorder(self, root):
	"""递归实现先序遍历"""
	if root == None:
		return
	print root.elem
	self.preorder(root.lchild)
	self.preorder(root.rchirld)

def inorder(self, root):
	"""递归实现中序遍历"""
	if root == None:
		return
	self.inorder(root.lchild)
	print root.elem
	self.inorder(root.rchirld)

def postorder(self, root):
	if root == None:
		return
	self.postorder(root.lchild)
	self.postorder(root.rchirld)
	print root.elem

"""Breadth First Search"""
def breadth_travel(self, root):
	"""利用队列实现树的层次遍历"""
	if root == None:
		return
	queue = []
	queue.append(root)
	while queue:
		node = queue.pop(0)
		print node.elem
		if node.lchild != None:
			queue.append(node.lchild)
		if node.rchirld != None:
			queue.append(node.rchirld)



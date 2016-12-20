class _DoubleLinkedBase:
	
	class _Node:
		
		def __init__(self,element,prevLink,nextLink):
			self._next=nextLink
			self._prev=prevLink
			self._element=element
		
	def __init__(self):
		self._header=self._Node(None,None,None)
		self._trailer=self._Node(None,None,None)
		self._header._next=self._trailer
		self._trailer._prev=self._header
		self._size=0
	
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def insert_between(self,element,predecessor,successor):
		newnode=self._Node(element,predecessor,successor)
		predecessor._next=newnode
		successor._prev=newnode
		self._size+=1
		return newnode
	
	def delete_node(self,node):
		predecessor=node._prev
		successor=node._next
		predecessor._next=successor
		successor._prev=predecessor
		self._size-=1
		element=node._element
		node._prev=node._next=node._element=None
		return element

class LinkedDequeue(_DoubleLinkedBase):
	
	def first(self):
		if self.is_empty():
			raise Empty('Queue is Empty')
		return self._header._next._element
	
	def last(self):
		if self.is_empty():
			raise Empty('Queue is Empty')
		return self._trailer._prev._element
	
	def insert_first(self,element):
		self.insert_between(element,self._header,self._header._next)
	
	def insert_last(self,element):
		self.insert_between(element,self._trailer._prev,self._trailer)
	
	def delete_first(self):
		if self.is_empty():
			raise Empty('Queue is Empty.')
		return self.delete_node(self._header._next)
	
	def delete_last(self):
		if self.is_empty():
			raise Empty('Queue is Empty.')
		return self.delete_node(self._trailer._prev)

class PositionalList(_DoubleLinkedBase):
	
	class Position:
		
		def __init__(self,container,node):
			self._container=container
			self._node=node
		
		def element(self):
			return self._node._element
		
		def __eq__(self,other):
			return type(other) is type(self) and other._node==self._node
		
		def __ne__(self,other):
			return not(self==other)
		
	
	def validate(self,p):
		if not isinstance(p,self.Position):
			raise TypeError('p must be proper position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._next is None:
			raise ValueError('p is not valid')
		return p._node
	
	def _make_position(self,node):
		if node is self._header or node is self._trailer:
			return None
		else:
			return self.Position(self,node)
	
	def first(self):
		return self._make_position(self._header._next)
	
	def last(self):
		return self._make_position(self._trailer._prev)
	
	def before(self,p):
		node=self.validate(p)
		return self._make_position(node._prev)
	
	def after(self,p):
		node=self.validate(p)
		return self._make_position(node._next)
	
	def __iter__(self):
		cursor=self.first()
		while cursor is not None:
			yield cursor.element()
			cursor=self.after(cursor)
	
	def insert_between(self,e,predecessor,successor):
		node=super().insert_between(e,predecessor,successor)
		return self._make_position(node)
	
	def add_first(self,e):
		return self.insert_between(e,self._header,self._header._next)
	
	def add_last(self,e):
		return self.insert_between(e,self._trailer._prev,self._trailer)
	
	def add_before(self,p,e):
		node=self.validate(p)
		return self.insert_between(e,node._prev,node)
	
	def add_last(self,p,e):
		node=self.validate(p)
		return self.insert_between(e,node,node._next)
	
	def delete(self,p):
		original=self.validate(p)
		return self.delete_node(original)
	
	def replace(self,p,e):
		node=self.validate(p)
		old_value=node._element
		node._element=e
		return old_value
	


if __name__=="__main__":
	myList=PositionalList()
	print(myList.first())
	myList.add_first(10)
	myList.add_first(20)
	myList.add_first(30)
	myList.add_first(40)
	myList.add_first(50)
	myList.add_first(60)
	print(myList.first().element())
	print(myList.last().element())
	toDel=myList.first()
	myList.delete(toDel)
	print(myList.first().element())

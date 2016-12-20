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
		(pos1,pos2)=self.find_insert_pos(element)
		print("The elements at position of insert is {0} and {1} ".format(pos1._element,pos2._element))
		self.insert_between(element,pos1,pos2)
	
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
		
		
		
	def find_insert_pos(self,element):
		#given an element find where this element should be inserted
		#returns the position of the node after which to be inserted
		#Assuming the list is already in sorted order
		
		if self._size==0:
			return (self._header,self._header._next)
		else:
			head=self._header._next
			if head._element>element:
				return (head._prev,head)
			while head._element is not None:
				if head._element>element:
					return (head._prev,head)
				head=head._next
			return (head,self._trailer)
	
if __name__=="__main__":
	myQueue=LinkedDequeue()
	myQueue.insert_first(10)
	myQueue.insert_first(20)
	myQueue.insert_first(30)

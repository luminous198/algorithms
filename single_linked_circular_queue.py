class Single_Linked_Circular_Queue:
	
	class _Node:
		
		def __init__(self,e,nextLink):
			self._element=e
			self._next=nextLink
		
	def __init__(self):
		self._tail=None
		self._size=0
	
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def first(self):
		if self.is_empty():
			raise Empty('Circular Queue is empty.')
		return self._tail._next._element
	
	def dequeue(self):
		if self.is_empty():
			raise Empty('Circular Queue is empty.')
		oldhead=self._tail._next
		if self._size==1:
			self._tail=None
		else:
			self._tail._next=oldhead._next
		self._size-=1
		return oldhead._element
	
	def enqueue(self,element):
		newest=self._Node(element,None)
		if self.is_empty():
			newest._next=newest
		else:
			newest._next=self._tail._next
			self._tail._next=newest
		self._tail=newest
		self._size+=1
	
	def rotate(self):
		if self._size>0:
			self._tail=self._tail._next

class Empty(Exception):
	pass
	
if __name__=="__main__":
	myCQueue=Single_Linked_Circular_Queue()
	print(myCQueue.__len__())
	myCQueue.enqueue(10)
	myCQueue.enqueue(20)
	myCQueue.enqueue(30)
	myCQueue.enqueue(40)
	print(myCQueue.dequeue())
	print(myCQueue.__len__())
	print(myCQueue.first())
	myCQueue.rotate()
	print(myCQueue.first())
	print(myCQueue.dequeue())
	print(myCQueue.dequeue())
	print(myCQueue.dequeue())
	print(myCQueue.dequeue())

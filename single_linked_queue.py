class SingleLinked_Queue:
	
	class _Node:
		
		def __init__(self,e,nextLink):
			self._element=e
			self._next=nextLink
			
	def __init__(self):
		self._head=None
		self._tail=None
		self._size=0
		
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def first(self):
		if self.is_empty():
			raise Empty('Queue is Empty')
		return self._head._element
	
	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is Empty')
		answer=self._head._element
		self._head=self._head._next
		self._size-=1
		if self.is_empty():
			self._tail=None
		return answer
	
	def enqueue(self,element):
		newest=self._Node(element,None)
		if self.is_empty():
			self._head=newest
		else:
			self._tail._next=newest
		self._tail=newest
		self._size+=1

class Empty(Exception):
	pass
	
if __name__=="__main__":
	myQueue=SingleLinked_Queue()
	print(myQueue.__len__())
	myQueue.enqueue(10)
	myQueue.enqueue(20)
	myQueue.enqueue(30)
	myQueue.enqueue(40)
	myQueue.enqueue(60)
	print(myQueue.first())
	print(myQueue.dequeue())
	print(myQueue.__len__())
	print(myQueue.dequeue())
	print(myQueue.dequeue())
	print(myQueue.dequeue())
	print(myQueue.first())
	print(myQueue.dequeue())
	print(myQueue.first())

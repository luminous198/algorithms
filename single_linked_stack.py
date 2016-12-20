class SingleLinkedStack:
	
	class _Node:
		
		__slots__='_element','_next'
		
		def __init__(self,element,nextLink):
			self._element=element
			self._next=nextLink
		
	def __init__(self):
		
		self._head=None
		self._size=0
		
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def push(self,e):
		self._head=self._Node(e,self._head)
		self._size+=1
	
	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element
	
	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		answer=self._head._element
		self._head=self._head._next
		self._size-=1
		return answer

class Empty(Exception):
	pass
	
if __name__=="__main__":
	myStack=SingleLinkedStack()
	print(myStack.__len__())
	myStack.push(10)
	myStack.push(20)
	print(myStack.top())
	print(myStack.pop())
	print(myStack.top())
	print(myStack.pop())
	print(myStack.top())	

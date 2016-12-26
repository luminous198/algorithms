class PQueue:
	def __init__(self):
		self.heapList = [(0,0)]
		self.currentSize = 0


	def percUp(self,i):
		#Compares keys according to the first element of the tuple
		while i // 2 > 0:
			if self.heapList[i][0] < self.heapList[i // 2][0]:
				tmp = self.heapList[i//2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i][0] > self.heapList[mc][0]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2][0] < self.heapList[i*2+1][0]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		#Returns the full tuple not just the key
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval
	
	def updateValue(self,item,newValue):
		'''
			Update the value for a given item.
			The key remains the same but the value changes. 
		'''
		done = False
		i=1
		key=0
		while not done and i<=self.currentSize:
			if self.heapList[i][1] == item:
				#Found the item to be updated make key point
				#to this item.
				done = True
				key = i
			else:
				i=i+1
		if key>0:
			self.heapList[key] = (self.heapList[key][0],newValue)
			
	def updateKey(self,item,value):
		'''
			Update the given item with the given value.
			The new key for this item becomes value.
		'''
		
		done = False
		i=1
		key=0
		while not done and i<=self.currentSize:
			if self.heapList[i][1] == item:
				#Found the item to be updated make key point
				#to this item.
				done = True
				key = i
			else:
				i=i+1
		if key>0:
			self.heapList[key] = (value,self.heapList[key][1])
			self.percUp(key)	
	'''
	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1
	'''
	def __str__(self):
		return str(self.heapList[1:])
	
	def heapSize(self):
		return self.currentSize
	
	def itemList(self):
		return self.heapList[1:]
		
def insertIntoQueue(pQ,itemList):
	for item in itemList:
		pQ.insert(item)

if __name__=='__main__':
	pQ=PQueue()
	itemList = [(999,'k'),(6,'s'),(8,'sd'),(100,'a'),(2,'b'),(17,'j'),(40,'d'),(12,'e'),(100,'f')]
	insertIntoQueue(pQ,itemList)
	print("The queue is")
	print(pQ)
	pQ.updateValue('k','g')
	print(pQ.itemList())
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	#print(pQ)
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	#print(pQ)
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	#print(pQ)
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))
	print("The item deleted from the queue is : {0}".format(pQ.delMin()))

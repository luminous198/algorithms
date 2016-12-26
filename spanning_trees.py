from graph import Graph
from priorityQueue import PQueue
from operator import itemgetter

def primJarnik(G,source = None):
	
	'''
		Compute the minimum spanning tree for a undirected graph.
		The minimum spanning tree is returned in a list called tree.It 
		contains the edges of the tree which can be printed.
		d is a dictionary which contains the bound to the distance from
		tree.
		queueList is a list in which all vertices of the graph are added
		and minimum edge is removed from it one at a time.
		vertexInList keeps track of which vertices are inside queueList.
		Each item in queueList is a tuple which has the form 
		(d[v],(v,edge)). 
	'''
	d = {}
	tree = []
	queueList = []
	vertexInList = []
	
	'''
		Create initial bound for the tree.
		The distance of source from the tree is 0 while for all other 
		vertices it is infinity.
		If the source is none , pick any source arbitarily from the 
		graph and start building the tree from there.
	'''
	maxDistance = float("inf")
	if source is None:
		vertexList = list(G.vertices())
		#Choose an arbitary source to run the algorith on
		source = vertexList[0]
	d[source] = 0
	
	for vertex in G.vertices():
		if vertex is not source:
			d[vertex] = maxDistance
	
	for vertex,value in d.items():
		queueList.append((value,(vertex,None)))
		vertexInList.append(vertex)
	
	while len(queueList)>0:
		'''
		Tind the item from list with least d value
		Pull this item from the list by deleting it from the list.
		Also delete this item from vertexInList structure as it no
		longer lives in the queueList structure.
		If this item has an edge then connect this item to the tree.
		'''
		minElement = min(queueList,key = lambda x : x[0])
		key,value = minElement
		u,edge = value
		queueList.remove(minElement)
		vertexInList.remove(u)
		if edge is not None:
			tree.append(edge)
		for e in G.incident_edges(u):
			v = e.opposite(u)
			if v in vertexInList:
				weight = e.element()
				if weight<d[v]:
					#We need to update v's data in the list queueList
					d[v] = weight
					'''
					Find the vertex for which we need to change the
					distance and edge related value in queueList.
					As the queueList list conatins nested tuples , the
					list is traversed to find the tuple which needs
					to be modified.
					Once the tuple is found a new tuple is created
					for that vertex.The new tuple is appended to the 
					list and the old tuple is removed.
					'''
					for elem in queueList:
						dist,vert = elem[0],elem[1]
						if vert[0] is v:
							newValue = (d[v],(v,e))
							queueList.append(newValue)
							queueList.remove(elem)
					
	return tree

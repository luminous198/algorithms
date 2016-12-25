from graph import Graph
from priorityQueue import PQueue

def djikstraShortestPath(G,source):
	'''
		A single source shortes path algorithm which computes shortest 
		path to all the vertices of a graph from a source given one
		exists.
		Graph must not contain negative cycles for the algorithm to work.
		Return dictionary mapping each reachable vertex to its distance 
		from src.
		
		d is a dictionary storing the distance of other vertices from 
		the source vertex.
		pQ is a priority Queue from which the vertex with the smallest 
		distance is popped.
		whenever a vertex is popped from the priority Queue it is added
		to the dictionary cloud and all its adjacent edges which are not
		in cloud are examined.
	'''
	
	d = {}
	cloud = {}
	pQ  = PQueue()
	
	
	maxDistance = float("inf")
	
	# for each vertex v of the graph, add an entry to the priority 
	# queue, with the source having distance 0 and all others having
	# infinite distance.
	for vertex in G.vertices():
		if vertex is source:
			d[vertex] = 0
		else: 
			d[vertex] = maxDistance
	
	for vertex,distance in d.items():
		pQ.insert((distance,vertex))
	
	while pQ.heapSize()>0:
		
		print("Now printing the heap.")
		for elem in pQ.itemList():
			print(elem[0],elem[1]._element)
		print("\n\n\n\n")
		'''
		Returns a tuple from the queue.
		The first element in the tuple is the distance d[v] and second
		is the vertex itself.
		'''
		key,u = pQ.delMin()
		print("The vertex popped from the heap is {0} with value {1}".format(u._element,key))
		cloud[u] = key
		for e in G.incident_edges(u):
			v = e.opposite(u)
			if v not in cloud:
				# perform relaxation step on edge (u,v)
				weight = e.element()
				if d[u] + weight < d[v]:
					d[v] = d[u] + weight #update the distance
					pQ.updateKey(v,d[v])
	return cloud
					
def shortes_path_tree(G,source,d):
	tree = {}
	for v in d:	
		if v is not source:
			for e in G.incident_edges(v,False):
				u = e.opposite(v)
				weight = e.element()
				if d[v] == d[u] + weight:
					tree[v] = e
	return tree

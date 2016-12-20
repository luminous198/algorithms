
class Graph:
	
	class Vertex:
	
		__slots__ = '_element'
		
		
		def __init__(self,x):
			self._element = x
		
		def element(self):
			return self._element
		
		def __hash__(self):
			return hash(id(self))
	
	class Edge:
		
		__slots__ = '_origin','_destination','_element'
		
		def __init__(self,u,v,x):
			self._origin = u
			self._destination = v
			self._element = x
		
		def endpoints(self):
			return (self._origin,self._destination)
		
		def opposite(self,v):
			return self._destination if v is self._origin\
				else self._origin
		
		def element(self):
			return self._element
		
		def __hash__(self):
			return hash((self._origin,self._destination)) 

	def __init__(self,directed=False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing
		self.dfs_clock = 1  #used to compute begin and end time for dfs
	
	def is_directed(self):
		return self._incoming is not self._outgoing
	
	def vertex_count(self):
		return len(self._outgoing)
	
	def vertices(self):
		return self._outgoing.keys()
	
	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		return total if self.is_directed() else total//2
	
	def edges(self):
		"Return a set of all edges of the graph"
		result = set()
		for secondary_map in self._outgoing.values():
			result.update(secondary_map.values())
		return result
	
	def get_edge(self,u,v):
		"Return edge from u to v or None if not adjacent"
		return self.outgoing[u].get(v)
	
	def degree(self,v,outgoing=True):
		'''
			Return number of outgoing edges incdent to vertex v in graph
			Can be used to return incoming if graph is directed.
		'''
		
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])
	
	def incident_edges(self,v,outgoing=True):
		'''
			Return all outgoing edges incident to vertex v in the graph.
			Can be used to return incoming if graph is directed.
		'''
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge
	
	def insert_vertex(self,x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming[v] = {}
		return v
	
	def insert_edge(self,u,v,x=None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e


def DFS_Complete(G):
	'''
		Do a depth first search on all vertices of the graph.
		Returns a depth first forest of the graph.
		The root of each tree points to None.
	'''
	startTime = {}
	finishTime = {}
	forest = {}
	for u in G.vertices():
		if u not in forest:
			startTime[u._element] = G.dfs_clock
			G.dfs_clock = G.dfs_clock+1
			forest[u] = None
			DFS(G,u,forest,startTime,finishTime)
	return (forest,startTime,finishTime)
	#Reset the clock after doing the DFS for further computations..
	G.dfs_clock = 1

def DFS(G,start,discovered,startTime,finishTime):
	'''
		Perform DFS of the graph starting from the vertex start.
		discovered is a hash table consisting of the edges used in DFS.
		discovered can be used to construct the path from between nodes.
	'''
	for e in G.incident_edges(start):
		neigh = e.opposite(start)
		if neigh not in discovered:
			startTime[neigh._element] = G.dfs_clock
			G.dfs_clock = G.dfs_clock+1
			discovered[neigh] = e
			DFS(G,neigh,discovered,startTime,finishTime)
	finishTime[start._element] = G.dfs_clock
	G.dfs_clock = G.dfs_clock+1	


def construct_path(u,v,discovered):
	'''
		Construct a path from u to v using discvered.
		Constructs path backwards starting from v and then revering the
		result.
	'''
	path = []
	if v in discovered:
		path.append(v)
		walk = v
		while walk is not u:
			e = discovered[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse
	return path

def BFS(G,start,discovered):
	'''
		Perform BFS of the graph starting at vertex start.
		discovered is a dictionary used to store which edge was used to
		discover which vertex.
		Start points to None in the discovery structure.
	'''
	level = [start]
	while len(level)>0:
		next_level = []
		for u in level:
			for e in G.incident_edges(u):
				v = e.opposite(u)
				if v not in discovered:
					discovered[v] = e
					next_level.append(v)
		level = next_level

def topologicalSort(G):
	'''
		Do a DFS of the graph.
		Print the nodes in the reverse order of their finish times of
		DFS.
	'''
	(discovered,startTime,finishTime) = DFS_Complete(G)
	print(sorted(finishTime.keys(),reverse=True))
	
	
if __name__ == "__main__":
	
	g = Graph(directed = True)
	u = g.insert_vertex('u')
	v = g.insert_vertex('v')
	x = g.insert_vertex('x')
	y = g.insert_vertex('y')
	w = g.insert_vertex('w')
	z = g.insert_vertex('z')
	print(g.vertex_count())
	g.insert_edge(u,v,2)
	g.insert_edge(u,x,1)
	g.insert_edge(x,v,9)
	g.insert_edge(v,y,10)
	g.insert_edge(y,x,11)
	g.insert_edge(w,y,12)
	g.insert_edge(w,z,13)
	g.insert_edge(z,z,14)
	print(g.edge_count())
	for edge in g.edges():
		print(edge._origin._element,\
				edge._destination._element,edge._element)
	
	
	
	discovered = {}
	(discovered,startTime,finishTime) = DFS_Complete(g)
	#path = construct_path(v1,v2,discovered)
	#path_order = []
	#for v in path:
	#	path_order.append(v._element)
	#print(path_order)
	
	print(startTime)
	print(finishTime)
	topologicalSort(g)	
	


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

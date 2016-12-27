from graph import Graph
from graph_functions_new import stronglyConnectedComponents
import operator
from single_linked_stack import SingleLinkedStack

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
			startTime[u] = G.dfs_clock
			G.dfs_clock = G.dfs_clock+1
			forest[u] = None
			DFS(G,u,forest,startTime,finishTime)
	G.dfs_clock = 1
	return (forest,startTime,finishTime)
	#Reset the clock after doing the DFS for further computations..
	

def DFS(G,start,discovered,startTime,finishTime):
	'''
		Perform DFS of the graph starting from the vertex start.
		discovered is a hash table consisting of the edges used in DFS.
		discovered can be used to construct the path from between nodes.
		startTime and finishTime record the start and finish time of the
		nodes being exmained respectively.
		Both are dictionaries mapping Vertices to integer values.
	'''
	for e in G.incident_edges(start):
		neigh = e.opposite(start)
		if neigh not in discovered:
			#Used for maze , knock down the wall
			#e.changeElement(1)
			startTime[neigh] = G.dfs_clock
			G.dfs_clock = G.dfs_clock+1
			discovered[neigh] = e
			DFS(G,neigh,discovered,startTime,finishTime)
	finishTime[start] = G.dfs_clock
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
		Return a list of verticies of directed acyclic graph g in topological order.
		If the graph has a cycle then the result will be incomplete. 
		
		topo is a list containg the final topological sort of the graph.
		ready is temporary stack used to input vertices when computing the topological sort.
		incount is a dictionary used to count the number of incoming edges for vertices.
		
		Topological Sort of the graph can also be used to test if the 
		graph is acyclic.
		If the graph has a cycle then the number of vertices returned
		by topologicalSort is less then total vertices in the graph,implying
		the sort if incomplete.
	'''
	
	topo = []
	ready = []
	incount = {}
	
	for vertex in G.vertices():
		incount[vertex] = G.degree(vertex,False) # Need incoming edges
		if incount[vertex] == 0:
			ready.append(vertex)
	
	while len(ready)>0:
		u = ready.pop()
		topo.append(u)
		for e in G.incident_edges(u):
			#There is an edge from u to v.
			#u has been added to topo, decrement the incoming edges to v
			v = e.opposite(u)
			incount[v] =incount[v]-1
			if incount[v] == 0:
				ready.append(v)
	return topo
	
def DFS_Complete_Iterative(G):
	'''
		Do a depth first search on all vertices of the graph.
		Returns a depth first forest of the graph.
		The root of each tree points to None.
	'''
	startTime = {}
	finishTime = {}
	forest = {}
	color = {}
	for vertex in G.vertices():
		color[vertex] = "white"
	
	for u in G.vertices():
		if u not in forest:
			startTime[u] = G.dfs_clock
			G.dfs_clock = G.dfs_clock+1
			forest[u] = None
			DFS_Iterative(G,u,forest,startTime,finishTime,color)
	G.dfs_clock = 1
	return (forest,startTime,finishTime)



def DFS_Iterative(G,start,discovered,startTime,finishTime,color):
	'''
		Runs an iterative depth-first Search on the graph.
		Discovered is a dictionary used to keep track of the vertices 
		which have been visited in the graph. 
		Color signifies different phases through which a vertex goes 
		when being examined.
		A vertex can have one of three colors at any given point:
		white,grey or black.Initially all vetices have color white.
		white->node has not been exmained yet
		grey->node is being examined
		black->node is finished being examined
		startTime and finishTime are dictionaries which store the start
		and finish times of the vertices respectively.
		dfs_clock is used to compute start and finish times.
		
		discovered -> dictionary mapping mapping vertices to edges 
		through which they were discovered.Helpful in figuring out the
		path through a vertex later.
		Color -> dictionary mapping vertices to colors.
		startTime ->dictionary mapping vertices to startTime.
		finishTime ->dictionary mapping vertices to finishTime.
		
	'''
	S = SingleLinkedStack()
	S.push(start)
	
	while(S.__len__()!=0):
		u = S.top()
		if color[u] is 'white':
			color[u] = 'grey'
			for e in G.incident_edges(u):
				neigh = e.opposite(u)
				if neigh not in discovered:
					#for maze
					e.changeElement(1)
					startTime[neigh] = G.dfs_clock
					G.dfs_clock = G.dfs_clock + 1
					discovered[neigh] = e
					S.push(neigh)
		elif color[u] is 'grey':
			u = S.pop()
			#print("popped from stack {0} ".format(S.pop()._element))
			color[u] = 'black'
			finishTime[u] = G.dfs_clock
			G.dfs_clock = G.dfs_clock + 1
	return (discovered,startTime,finishTime)
	


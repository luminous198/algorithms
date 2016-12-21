from graph import Graph
from graph_functions_new import stronglyConnectedComponents
import operator

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
	return (forest,startTime,finishTime)
	#Reset the clock after doing the DFS for further computations..
	G.dfs_clock = 1

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
		Do a DFS of the graph.
		Return the vertices in the reverse order of their finish times of
		DFS in a list.
	'''
	(discovered,startTime,finishTime) = DFS_Complete(G)
	
	finishTimeList = sorted(finishTime.items(),key = operator.itemgetter(1),reverse=True)
	finishTimeList = [x[0] for x in finishTimeList]
	return finishTimeList

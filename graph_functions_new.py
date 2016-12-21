from graph import Graph
import operator
import graph_functions as graph_func

def reverseGraph(G,directed = True):
	'''
		Given a graph G finds and returns its inverse.
		Assumes a directed graph by default.
	'''
	
	reverseG = Graph(directed = True)
	#Add all vertices of G to reverseG
	for key in G._outgoing:
		reverseG._outgoing[key] = {}
		reverseG._incoming[key] = {}
	
	for key,value in G._outgoing.items():
		vertex = key
		edges = value
		
		for v,w in edges.items():
			reverG.insert_edge(v,vertex,w)
		
def stronglyConnectedComponents(G):
	
	(forest,startTime,finishTime) = graph_func.DFS_Complete(G)
	
	'''
	Sort the finishTime into decreasing order of finishTime.
	finishTime is a dictionary consisting of vertices and finish
	time values.
	finishTimeList is a list which stores vertices in order of their
	decreasing finish times.
	'''
	finishTimeList = sorted(finishTime.items(),key = operator.itemgetter(1),reverse=True)
	finishTimeList = [x[0] for x in finishTimeList]
	(SCC_forest,startTime,finishTime) = DFS_Complete_SCC(G,finishTimeList)
	return (SCC_forest,startTime,finishTime)
	
	
def DFS_Complete_SCC(reverseG,finishTimeList):
	'''
		Start doing the DFS according to the finishTimeList.
	'''
	
	startTime = {}
	finishTime = {}
	forest = {}
	for u in finishTimeList:
		if u not in forest:
			startTime[u] = reverseG.dfs_clock
			reverseG.dfs_clock = reverseG.dfs_clock+1
			forest[u] = None
			DFS_SCC(reverseG,u,forest,startTime,finishTime)
	return (forest,startTime,finishTime)
	#Reset the clock after doing the DFS for further computations..
	reverseG.dfs_clock = 1
	
def DFS_SCC(reverseG,start,discovered,startTime,finishTime):
	'''
		Perform DFS of the graph starting from the vertex start.
		discovered is a hash table consisting of the edges used in DFS.
		discovered can be used to construct the path from between nodes.
	'''
	for e in reverseG.incident_edges(start,outgoing = False):
		neigh = e.opposite(start)
		if neigh not in discovered:
			startTime[neigh] = reverseG.dfs_clock
			reverseG.dfs_clock = reverseG.dfs_clock+1
			discovered[neigh] = e
			DFS_SCC(reverseG,neigh,discovered,startTime,finishTime)
	finishTime[start] = reverseG.dfs_clock
	reverseG.dfs_clock = reverseG.dfs_clock+1	
	

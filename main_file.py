from graph import Graph
import graph_functions as graph_func
import graph_functions_new as graph_func_new


def testFunction(g):
	#Tests the topological sort using DFS
	topSort = graph_func.topologicalSort(g)
	topSort = [x._element for x in topSort]
	print("The topological sort of the graph is {0} ".format(topSort))
	print("\n\n\n\n\n\n")
	
	#Tests the strongly connected components for graph
	(SCC_forest,startTime,finishTime) = graph_func_new.stronglyConnectedComponents(g)	
	print("The vertices with strongly connected compnents are : ")
	for vertex in SCC_forest:
		if SCC_forest[vertex] is None:
			print(vertex._element)
	print('\n\n\n')
		
	
	#Tests the topological sort using iterative DFS
	topSortIter = graph_func.topologicalSortIterative(g)
	topSortIter = [x._element for x in topSortIter]
	print("The topological sort of the graph using iterative DFS is {0} ".format(topSortIter))

def printGraph(G,directed=False):
	print("Print the graph.")
	for vertex,adj in G._outgoing.items():
		for neigh,value in adj.items():
			print(vertex._element,neigh._element,value._element)
	
	if directed:
		print("Print the reverse graph.")
		for vertex,adj in G._incoming.items():
			for neigh,value in adj.items():
				print(vertex._element,neigh._element,value._element)
	
def insertEdgesList(G,edgeList):
	'''
		Takes a list of edges to be put in the graph.
		edgeList contains tuples of information on edges.
		First item in each tuple is originating vertex, Second item is the
		destination vertex and third is the value for the edge.
	'''
	
	for edge in edgeList:
		G.insert_edge(edge[0],edge[1],edge[2])

def showGraphInfo(G):
	print("Number of vertices in the graph : {0}".format(g.vertex_count()))
	vertex_list = []
	for vertex in G.vertices():
		vertex_list.append(vertex._element)
	print("List of Vertces in the graph : {0}".format(vertex_list))
	
	print("Number of Edges in the graph: {0}".format(G.edge_count()))
	print("List of edges in the graph")
	for edge in G.edges():
		print("{0} ----> {1} with value {2}".format(edge._origin._element,\
				edge._destination._element,edge._element))
if __name__ == "__main__":
	
	g = Graph(directed = True)
	u = g.insert_vertex('u')
	v = g.insert_vertex('v')
	x = g.insert_vertex('x')
	y = g.insert_vertex('y')
	w = g.insert_vertex('w')
	z = g.insert_vertex('z')
	print("Number of vertices in the graph: {0}".format(g.vertex_count()))
	
	edgeList = [(u,v,2),(u,x,1),(x,v,9),(v,y,10),\
				(y,x,11),(w,y,12),(w,z,13),(z,z,14)]
	insertEdgesList(g,edgeList)
	showGraphInfo(g)
	
	
	
	
	
	

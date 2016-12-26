from graph import Graph
import graph_functions as graph_func
import graph_functions_new as graph_func_new
import shortest_path as sh_paths
import spanning_trees as sp_tree

def testFunction(g):
	
	#Prints the topological sort of the graph.
	#Prints error message of the graph has cycle(s).
	topSort = graph_func.topologicalSort(g)
	if len(topSort)!=g.vertex_count():
		print("The graphs has cycles.Topological sort incomplete.")
	else:
		topSort = [x._element for x in topSort]
		print(topSort)
	
	#Tests the strongly connected components for graph
	(SCC_forest,startTime,finishTime) = graph_func_new.stronglyConnectedComponents(g)	
	print("The vertices with strongly connected compnents are : ")
	for vertex in SCC_forest:
		if SCC_forest[vertex] is None:
			print(vertex._element)
	print('\n\n\n')

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
	print("Number of vertices in the graph : {0}".format(G.vertex_count()))
	vertex_list = []
	for vertex in G.vertices():
		vertex_list.append(vertex._element)
	print("List of Vertces in the graph : {0}".format(vertex_list))
	
	print("Number of Edges in the graph: {0}".format(G.edge_count()))
	print("List of edges in the graph")
	for edge in G.edges():
		print("{0} ----> {1} with value {2}"\
						.format(edge._origin._element,\
						edge._destination._element,\
						edge._element))

def shortestPathDjisktra(G,source):
	
	#Run djikstra's algorithm from the given source
	djikstraOutput = sh_paths.djikstraShortestPath(G,source)
	for key,value in djikstraOutput.items():
		print("The distance of vertex {0}from source vertex {1} is {2}"\
				.format(key._element,u._element,value))
	

def shortestPathBellmanFord(G,source):	
	bellmanfordOutput= sh_paths.bellman_ford_algorithm(g,u)
	if bellmanfordOutput[0] is False:
		print("There are negative weight cycles in the graph. Cannot compute shortest paths.")
	else:
		for key,value in bellmanfordOutput[1].items():
			print("The distance of vertex {0} from source vertex {1} is {2} ".format(key._element,u._element,value))

def spanningTreePrimJarnik(G,source=None):
	primTree = sp_tree.primJarnik(g,source)
	print("Now printing the edges in the MST")
	print("The number of edges in the tree is {0} ".format(len(primTree)))
	for edge in primTree:
		print("{0} ----> {1} with value {2}"\
						.format(edge._origin._element,\
						edge._destination._element,\
						edge._element))

if __name__ == "__main__":
	
	g = Graph(directed = False)
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
	
	

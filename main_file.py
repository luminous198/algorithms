from graph import Graph
import graph_functions as graph_func
import graph_functions_new as graph_func_new

	
if __name__ == "__main__":
	
	g = Graph(directed = True)
	u = g.insert_vertex('u')
	v = g.insert_vertex('v')
	x = g.insert_vertex('x')
	y = g.insert_vertex('y')
	w = g.insert_vertex('w')
	z = g.insert_vertex('z')
	print("Number of vertices in the graph: {0}".format(g.vertex_count()))
	g.insert_edge(u,v,2)
	g.insert_edge(u,x,1)
	g.insert_edge(x,v,9)
	g.insert_edge(v,y,10)
	g.insert_edge(y,x,11)
	g.insert_edge(w,y,12)
	g.insert_edge(w,z,13)
	g.insert_edge(z,z,14)
	print("Number of Edges in the graph: {0}".format(g.edge_count()))
	print("List of edges in the graph")
	for edge in g.edges():
		print("{0} ----> {1} with value {2}".format(edge._origin._element,\
				edge._destination._element,edge._element))
	print("\n\n\n\n\n\n")
	
	topSort = graph_func.topologicalSort(g)
	topSort = [x._element for x in topSort]
	print("The topological sort of the graph is {0} ".format(topSort))
	print("\n\n\n\n\n\n")
	
	(SCC_forest,startTime,finishTime) = graph_func_new.stronglyConnectedComponents(g)	
	print("The vertices with strongly connected compnents are : ")
	for vertex in SCC_forest:
		if SCC_forest[vertex] is None:
			print(vertex._element)
	

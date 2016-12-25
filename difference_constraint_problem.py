from graph import Graph
import shortest_path as sh_paths
import main_file as temp_func
import shortest_path as sh_paths

def convertMatrixToGraph(matrixA,matrixB):
	'''
		Given a matrix of mxn elements.
		Convert the given matrices to a graph.
		Returns a tuple containing the graph and a dictionary called 
		vertList which maps the name of the vertex to the vertex itself.
		
		Eg:
		
		| 1 -1  0  0  0 |                |  0 |
		| 1  0  0  0 -1 |  | x1 |        | -1 |
		| 0  1  0  0 -1 |  | x2 |		 |  1 |
		|-1  0  1  0  0 |  | x3 |   ==   |  5 |
		|-1  0  0  1  0 |  | x4 |        |  4 |
		| 0  0 -1  1  0 |  | x5 |        | -1 |
		| 0  0 -1  0  1 |                | -3 |
		| 0  0  0 -1  1 |                | -3 |
		
		This above matrices represent the follwing problem:
		
		x1-x2<=0
		x1-x5<=-1
		x2-x5<=1
		x3-x1<=5
		x4-x1<=4
		x4-x3<=-1
		x5-x3<=-3
		x5-x4<=-3
		
		The variables x1,x2,x3.....xn become the vertices of the graph.
		The graph has one additional vertex x0.
		The vertices are named as Vertex0,Vertex1......Vertexn.They are
		stored in a dictionary called vertList.
		There is an edge in the graph with the vertex with the negative
		sign as the source vertex and the vertex with the positive sign
		as the destination vertex.
		The weight of the edge is the value on right side of the 
		equation.
		
		x1-x2<=0 means there is an edge from x2 to x1 with weight 0.
		
		There are edges from vertex x0 to all other vertices with a 
		weight of 0.  
		
	'''
	numVariables = len(matrixA[0])
	#Make a graph with numVariables +1 vertices
	g = Graph(directed = True)
	v0 = g.insert_vertex("Vertex" + str(0))
	vertList = {}
	vertList[0] = v0
	for i in range(1,numVariables+1):
		vertList[i] = g.insert_vertex("Vertex" + str(i))
	i=0
	for key,value in vertList.items():
		if key is not 0:
			g.insert_edge(vertList[0],vertList[key],0)
	for elem in matrixA:
		origin = elem.index(-1) + 1
		destination = elem.index(1) + 1
		weight = matrixB[i]
		i = i+1
		g.insert_edge(vertList[origin],vertList[destination],weight)
	#temp_func.showGraphInfo(g)
	return (g,vertList)

def findSolution(G,vertList):
	
	'''
		Takes as input a graph and a dictionary which contains the 
		mapping of vertex names to the vertex.
		Uses bellman ford algorithm to compute the result.
		If the result cannot be computed returns None object as the 
		answer.
		If the result is computed returns a list which contains the 
		solution to the set of equations.
		The list has length n for n variables in sorted order.
		
		Generating the ouput format:
		bellmanfordOutput[1] is a dictionary which contains mapping
		of vertex to their shortest path values.
		This dictionary is first converted into a list called listOutput
		listOutput is used to create a list with names of vertices 
		instead of the vertices themselves  called result.
		result is sorted according to the names of the vertices.
		The result list is returned with only the shortest path 
		excluding the vertex names and the first value is also 
		discarded as vertex0 was added initially as the source. 
	'''
	u = vertList[0]	
	bellmanfordOutput= sh_paths.bellman_ford_algorithm(G,u)
	if bellmanfordOutput[0] is False:
		print("There are negative weight cycles in the graph. Cannot compute shortest paths.")
		return None
	else:
		result = []
		listOutput = bellmanfordOutput[1].items()
		for elem in listOutput:
			result.append((elem[0]._element,elem[1]))
		result = sorted(result,key = lambda x:x[0])
		result = [elem[1] for elem in result[1:]]
		return result
	
if __name__ == "__main__":
	
	
	matrixA = [[1,-1,0,0,0],[1,0,0,0,-1],[0,1,0,0,-1],[-1,0,1,0,0],[-1,0,0,1,0],[0,0,-1,1,0],[0,0,-1,0,1],[0,0,0,-1,1]]
	matrixB = [0,-1,1,5,4,-1,-3,-3]
	graph,vertList = convertMatrixToGraph(matrixA,matrixB)
	print(findSolution(graph,vertList))

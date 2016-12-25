from graph import Graph
import shortest_path as sh_paths
import main_file as temp_func
import shortest_path as sh_paths

def convertMatrixToGraph(matrixA,matrixB):
	
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
	result = []
	u = vertList[0]	
	bellmanfordOutput= sh_paths.bellman_ford_algorithm(G,u)
	if bellmanfordOutput[0] is False:
		print("There are negative weight cycles in the graph. Cannot compute shortest paths.")
		return None
	else:
		newList = []
		listOutput = bellmanfordOutput[1].items()
		for elem in listOutput:
			newList.append((elem[0]._element,elem[1]))
		newList = sorted(newList,key = lambda x:x[0])
		result = [elem[1] for elem in newList[1:]]
		return result
	
if __name__ == "__main__":
	
	'''
		Given a matrix of mxn elements.Compute the answer to the
		difference constraint equation using shortest paths in graphs.
		
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
		
	'''
	matrixA = [[1,-1,0,0,0],[1,0,0,0,-1],[0,1,0,0,-1],[-1,0,1,0,0],[-1,0,0,1,0],[0,0,-1,1,0],[0,0,-1,0,1],[0,0,0,-1,1]]
	matrixB = [0,-1,1,5,4,-1,-3,-3]
	graph,vertList = convertMatrixToGraph(matrixA,matrixB)
	print(findSolution(graph,vertList))

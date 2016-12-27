from graph import Graph
import main_file as mf
import graph_functions as graph_func
import main_file as mf
import operator
from single_linked_stack import SingleLinkedStack

def makeMaze(boardSize):
	
	'''
		Model a maze as a graph.
		
		Though the maze is modeled as a graph but think of it like a 
		chess board of arbitary boardSize.
		
		Consider the follwoing board when boardSize=4:
		
		|12 13 14 15 |
		| 8  9 10 11 |
		| 4  5  6  7 |
		| 0  1  2  3 |
		
		The numberings are made by converting the two dimensional for
		loop into one dimension.
		These numbers become the vertices of the graph.
		
		Edges are added between vertices if adding an edge between two
		vertices generates a valid move.
		For eg : valid moves for vertex 5 : 4,9,1,6
				 valid moves for vertex 4 : 8,5,0
		
		The value of edge represents either a open path or a blockade.
		If the value of edge is 1 then that path is open else if value
		is 0 then the path is closed.
		Initally the value of each edge is given as 0.
		Specific maze generating algorithms can be used to create mazes
		from the provided representation.
		
		Returns the graph g and vertList structure.
		The vertList structure is a dictionary used to identify all the
		vertices of the graph.
		The key for each vertex is an integer and the value is the 
		vertex itself.
	'''
	
	
	g= Graph()
	vertList = {}
	
	for i in range(boardSize):
		for j in range(boardSize):
			vertexID = convertIntoOneDim(i,j,boardSize)
			vertList[vertexID] = g.insert_vertex(vertexID)
	
	for i in range(boardSize):
		for j in range(boardSize):
			#Now generate and insert edges into the graph
			fromVertex = convertIntoOneDim(i,j,boardSize)
			validPositions = generateLegalMoves(i,j,boardSize)
			for elem in validPositions:
				toVertex = convertIntoOneDim(elem[0],elem[1],boardSize)
				g.insert_edge(vertList[fromVertex],vertList[toVertex],0)
	return (g,vertList)
		
def legalOffsets(x,y,boardSize):
	'''
		Check if the given coordinates are within the bounds of the
		board or not.Use to generate legal moves for a given position.
	'''
	return x>=0 and x<boardSize and y>=0 and y<boardSize
	
def generateLegalMoves(x,y,boardSize):
	'''
		Generate legal moves for a given position in the 2-D matrix.
		The legal moves can be laft,right,up,down but some of these
		moves can be illegal too.For eg going left from vertex 4 counts
		as an illegal move.
		Every moveOffset is checked with legalOffsets function to make
		sure that the new coordinates are within the bounds of the 
		graph. 
	'''
	moveList = []
	moveOffsets = [(-1,0),(1,0),(0,1),(0,-1)]
	for elem in moveOffsets:
		newX = x+elem[0]
		newY = y+elem[1]
		if legalOffsets(newX,newY,boardSize):
			moveList.append((newX,newY))
	return moveList
		

def convertIntoOneDim(x,y,boardSize):
	'''
		Converts a two dimensional point to 1 dimension.
		For eg : Given a boardSize of 4 : 
		Elements of second row are 4,5,6,7 which can be generated
		as 4(1) + (0,1,2,3)  
	'''
	
	return boardSize*x+y

def showGraphInfo(G):
	print("Number of vertices in the graph : {0}".format(G.vertex_count()))
	vertex_list = []
	for vertex in G.vertices():
		vertex_list.append(vertex._element)
	#print("List of Vertces in the graph : {0}".format(vertex_list))
	
	print("Number of Edges in the graph: {0}".format(G.edge_count()))
	#print("List of edges in the graph")
	count = 0 
	for edge in G.edges():
		if edge.element()==1:
	#		print("{0} ----> {1} with value {2}"\
	#						.format(edge._origin._element,\
	#						edge._destination._element,\
	#						edge._element))
			count = count+1
		
	print("Number of knocked down walls is {0} ".format(count))

def Maze_Generator_DFS(G):
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
			Maze_Generator_DFS_Hepler(G,u,forest,startTime,finishTime,color)
	G.dfs_clock = 1
	return (forest,startTime,finishTime)



def Maze_Generator_DFS_Hepler(G,start,discovered,startTime,finishTime,color):
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


	
if __name__ == "__main__":
	(g,vertList) = makeMaze(100)
	
	(forest,startTime,finishTime) = Maze_Generator_DFS(g)
	showGraphInfo(g)
	#for key,value in startTime.items():
	#	print(""key._element,value)
	source = min(list(startTime.items()),key = lambda x :x[1])
	#print(source[0]._element,source[1])
	print("The starting vertex of the maze is {0}.".format(source[0]._element))
	
	#primTree = primJarnik(g,source[0])
	#print("Now printing the edges in the MST")
	#print("The number of edges in the tree is {0} ".format(len(primTree)))
	'''
	for edge in primTree:
		print("{0} ----> {1} with value {2}"\
						.format(edge._origin._element,\
						edge._destination._element,\
						edge._element))
	'''

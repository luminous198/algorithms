from graph import Graph
import main_file as mf

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

if __name__ == "__main__":
	(g,vertList) = makeMaze(4)
	mf.showGraphInfo(g)

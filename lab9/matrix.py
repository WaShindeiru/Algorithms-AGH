class Vertex:
    def __init__(self, key, brightness=0):
        self.key = key
        self.brightness = brightness

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return str(self.key)

class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __repr__(self):
        return str(self.weight)

    def __eq__(self, other):
        return self.key == other.key and self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2    

class Graph:
    def __init__(self):
        self.vertexTable = list()
        self.vertexDictionary = dict()
        self._size = 0
        self._order = 0
        self.freeIndices = list()

    def isEmpty(self):
        return self._size == 0

    def getVertexIdx(self, vertex):
        return self.vertexDictionary.get(vertex, None)

    def getVertex(self, index):
        return self.vertexTable[index]

    def order(self):
        return self._order

    def size(self):
        return self._size

    def setBrightness(self, vertex, brightness):
        self.vertexTable[vertex].brightness = brightness

class AdjListGraph(Graph):
    def __init__(self, graph = None):
        if graph is None:
            Graph.__init__(self)
            self.adjList = list()

        else:
            for edge in graph:
                self.insertVertex(Vertex(edge[0]))
                self.insertVertex(Vertex(edge[1]))
                self.insertEdge(edge[0], edge[1], edge[2])

    def deleteEdge(self, vertex1, vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        if index2 is None or index1 is None:
            return

        if self.adjList[index1].get(vertex2, None) == None:
            return

        del self.adjList[index1][vertex2]
        del self.adjList[index2][vertex1]

        self._size -= 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        if index is None:
            return

        self.vertexTable[index] = None
        del self.vertexDictionary[vertex]

        for x in range(len(self.adjList)):
            self.adjList[x].pop(vertex, 0)

        self.adjList[index] = None

        self.freeIndices.append(index)

        self._order -= 1

    def insertVertex(self, vertex):
        if vertex in self.vertexDictionary:
            return

        if self.freeIndices:
            index = self.freeIndices.pop(0)
            self.vertexTable[index] = vertex

        else:
            index = len(self.vertexTable)
            self.vertexTable.append(vertex)
            self.adjList.append(dict())

        self.vertexDictionary[vertex] = index
        self._order += 1

        return vertex

    def insertEdge(self, vertex1, vertex2, edge):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        
        if vertex2 not in self.adjList[index1]:
            self._size += 1

        self.adjList[index1][vertex2] = Edge(vertex1, vertex2, edge)
        self.adjList[index2][vertex1] = Edge(vertex2, vertex1, edge)

    def neighbours(self, vertex_idx):
        return [(x, self.adjList[vertex_idx][x]) for x in self.adjList[vertex_idx]]

    # def neighboursIdx(self, vertex):
    #     return list(self.adjList[self.getVertexIdx(vertex)].keys())

    def neighbourEdgesIdx(self, idx):
        return list(self.adjList[idx].values())

    def neighbourEdges(self, vertex):
        return list(self.adjList[self.getVertexIdx(vertex)].values())

    def edges(self):
        edges = set()
        indices = self.vertexDictionary.values()

        for i in indices:
            temp = self.adjList[i]
            for y in temp:
                edges.add((self.getVertex(i).key, y.key))

        return list(edges)

    def vertices(self):
        return list(self.vertexDictionary.keys())

class AdjMatrixGraph(Graph):
    def __init__(self):
        self.adjMatrix = list()
        self.realSize = 0
        super().__init__()

    def insertVertex(self, vertex):
        if self.getVertexIdx(vertex) is not None:
            return

        if self.freeIndices:
            index = self.freeIndices.pop()
            self.vertexTable[index] = vertex
            self.adjMatrix[index] = [None for x in range(self.realSize)]
            self.vertexDictionary[vertex] = index

            for x in self.vertexDictionary.values():
                self.adjMatrix[x][index] = 0
                self.adjMatrix[index][x] = 0

            self._order += 1

        else:
            index = Graph.order(self)
            self._order += 1
            self.vertexTable.append(vertex)
            self.vertexDictionary[vertex] = index
            self.adjMatrix.append([0 for x in range(self._order)])
            for x in range(self._order):
                if x != index:
                    self.adjMatrix[x].append(0)

        self.realSize += 1

    def insertEdge(self, vertex1, vertex2, edge):
        index1 = Graph.getVertexIdx(self, vertex1)
        index2 = Graph.getVertexIdx(self, vertex2)
        if index1 is None or index2 is None:
            return

        self.adjMatrix[index1][index2] = 1
        self.adjMatrix[index2][index1] = 1

        self._size += 1

    def neighboursIdx(self, vertex_idx):
        temp = list()
        for index, val in enumerate(self.adjMatrix[vertex_idx]):
            if val > 0:
                temp.append(index)

        return temp

    def neighbours(self, vertex_idx):
        neighbours = self.neighboursIdx(vertex_idx)
        return [Graph.getVertex(self, index) for index in neighbours]

    def deleteEdge(self, vertex1, vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        if index1 is None or index2 is None:
            return

        if self.adjMatrix[index1][index2] == 1:
            self.adjMatrix[index1][index2] = 0
            self.adjMatrix[index2][index1] = 0
            self._size -= 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        if index is None:
            return

        del self.vertexDictionary[vertex]
        self.vertexTable[index] = None
        self.adjMatrix[index] = None

        for i in self.vertexDictionary.values():
            self.adjMatrix[i][index] = None

        self._order -= 1
        self.freeIndices.append(index)

    def edges(self):
        temp = list()
        for x in self.vertexDictionary.values():
            for y in range(0, x, 1):
                if self.adjMatrix[x][y] is not None and self.adjMatrix[x][y] > 0:
                    temp.append((self.getVertex(x).key, self.getVertex(y).key))

        return temp


def main():
    graph = AdjListGraph()
    
    a1 = graph.insertVertex(Vertex("aha"))
    a2 = graph.insertVertex(Vertex("kurwa"))
    a3 = graph.insertVertex(Vertex("Deszcz"))

    graph.insertEdge(a1, a2, 2)
    graph.insertEdge(a1, a3, 2)

    neighbours = graph.neighboursIdx(graph.getVertexIdx(a1))

    print([graph.getVertexIdx(i) for i in graph.neighboursIdx(graph.getVertexIdx(a1))])



def main2():

    graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    
    ExampleGraph = AdjListGraph()
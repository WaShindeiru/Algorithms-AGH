#Skończone
import polska


class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Graph:
    def __init__(self):
        self.vertexTable = list()
        self.vertexDictionary = dict()
        self.size = 0
        self.order = 0
        self.freeIndices = list()

    def isEmpty(self):
        return self.size == 0

    def getVertexIdx(self, vertex):
        return self.vertexDictionary.get(vertex, None)

    def getVertex(self, index):
        return self.vertexTable[index]

    def order(self):
        return self.order

    def size(self):
        return self.size

class AdjListGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.adjList = list()

    def deleteEdge(self, vertex1, vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)
        if index2 is None or index1 is None:
            return

        for index, value in enumerate(self.adjList[index1]):
            if value == index2:
                self.adjList[index1].pop(index)

        for index, value in enumerate(self.adjList[index2]):
            if value == index1:
                self.adjList[index2].pop(index)

        self.size -= 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        if index is None:
            return

        self.vertexTable[index] = None
        del self.vertexDictionary[vertex]

        for x in range(len(self.adjList)):
            for ind, vertex2 in enumerate(self.adjList[x]):
                if vertex2 == index:
                    del self.adjList[x][ind]

        self.adjList[index] = None

        self.freeIndices.append(index)

        self.order -= 1

    def insertVertex(self, vertex):
        if self.freeIndices:
            index = self.freeIndices.pop(0)
            self.vertexTable[index] = vertex

        else:
            index = len(self.vertexTable)
            self.vertexTable.append(vertex)
            self.adjList.append(list())

        self.vertexDictionary[vertex] = index
        self.order += 1

    def insertEdge(self, vertex1, vertex2, edge):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)

        for vertex in self.adjList[index1]:
            if index2 == vertex:
                return

        self.adjList[index1].append(index2)
        self.adjList[index2].append(index1)

        self.size += 1

    def neighboursIdx(self, vertex_idx):
        return self.adjList[vertex_idx][:]

    def edges(self):
        edges = set()
        indices = self.vertexDictionary.values()

        for i in indices:
            temp = self.adjList[i]
            for y in temp:
                edges.add((self.getVertex(i).key, self.getVertex(y).key))

        return list(edges)

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

            self.order += 1

        else:
            index = Graph.order(self)
            self.order += 1
            self.vertexTable.append(vertex)
            self.vertexDictionary[vertex] = index
            self.adjMatrix.append([0 for x in range(self.order)])
            for x in range(self.order):
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

        self.size += 1

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
            self.size -= 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        if index is None:
            return

        del self.vertexDictionary[vertex]
        self.vertexTable[index] = None
        self.adjMatrix[index] = None

        for i in self.vertexDictionary.values():
            self.adjMatrix[i][index] = None

        self.order -= 1
        self.freeIndices.append(index)

    def edges(self):
        temp = list()
        for x in self.vertexDictionary.values():
            for y in range(0, x, 1):
                if self.adjMatrix[x][y] is not None and self.adjMatrix[x][y] > 0:
                    temp.append((self.getVertex(x).key, self.getVertex(y).key))

        return temp


def main():
    # test dla grafu z wykorzystaniem macierzy sąsiedztwa
    vertices = set([number for sublist in polska.graf for number in sublist])

    graph = AdjMatrixGraph()
    for key in vertices:
        graph.insertVertex(Vertex(key))

    for edge in polska.graf:
        graph.insertEdge(Vertex(edge[0]), Vertex(edge[1]), 1)

    graph.deleteVertex(Vertex("K"))
    graph.deleteEdge(Vertex("E"), Vertex("W"))
    graph.deleteEdge(Vertex("W"), Vertex("E"))
    polska.draw_map(graph.edges())


def main2():
    # test dla grafu z wykorzystaniem listy sąsiedztwa
    vertices = set([number for sublist in polska.graf for number in sublist])

    graph = AdjListGraph()
    for key in vertices:
        graph.insertVertex(Vertex(key))

    for edge in polska.graf:
        graph.insertEdge(Vertex(edge[0]), Vertex(edge[1]), 1)

    graph.deleteVertex(Vertex("K"))
    graph.deleteEdge(Vertex("E"), Vertex("W"))
    graph.deleteEdge(Vertex("W"), Vertex("E"))
    polska.draw_map(graph.edges())


if __name__ == "__main__":
    main()

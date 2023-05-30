import numpy as np


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

    def toNumpyArray(self):
        return np.array(self.adjMatrix)


def main():
    temp = AdjMatrixGraph()
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")

    temp.insertVertex(vertex1)
    temp.insertVertex(vertex2)
    temp.insertVertex(vertex3)

    temp.insertEdge(vertex1, vertex2, 1)
    temp.insertEdge(vertex2, vertex3, 1)

    print(temp.toNumpyArray())

main()
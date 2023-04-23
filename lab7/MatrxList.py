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

        for i in range(len(self.adjList[index1])):
            if self.adjList[index1][i] == index2:
                self.adjList[index1].pop(i)
                break

        self.size -= 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
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

        self.adjList[index1].append(index2)
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
    def __inti__(self):
        Graph.__init__(self)


def main():
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

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
        self.adjList = list()
        self.freeIndices = list()

    def isEmpty(self):
        return self.size == 0

    def insertVertex(self, vertex):
        index = len(self.vertexTable)
        self.vertexTable.append(vertex)
        self.vertexDictionary[vertex] = index
        self.adjList.append(list())
    
    def insertEdge(self, vertex1, vertex2):
        index1 = self.getVertexIdx(vertex1)
        index2 = self.getVertexIdx(vertex2)

        self.adjList[index1].append(index2)

    def getVertexIdx(self, vertex):
        return self.vertexDictionary[vertex]

    def getVertex(self, index):
        return self.vertexTable[index]

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

def main():
    example = Graph()
    temp = Vertex("RJS")
    temp2 = Vertex("KRK")
    temp3 = Vertex("WW")
    example.insertVertex(temp)
    example.insertVertex(temp2)
    example.insertVertex(temp3)
    example.insertEdge(temp, temp2)
    example.insertEdge(temp, temp3)
    # aha = example.getVertexIdx(temp)
    # print(aha)
    # print(example.getVertex(aha).key)

    print(example.edges())

if __name__ == "__main__":
    main()

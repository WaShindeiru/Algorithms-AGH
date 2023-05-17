from matrix import *

def prim_algorithm(graph, start):

    newGraph = AdjListGraph()
    
    intree = [False for i in range(graph.order())]
    distance = [float('inf') for i in range(graph.order())]
    parent = [-1 for i in range(graph.order())]

    distance[start] = 0
    current_vertex = start

    newGraph.insertVertex(graph.getVertex(current_vertex))

    while(intree[current_vertex] == False):

        intree[current_vertex] = True
        edges = graph.neighbourEdgesIdx(current_vertex)

        while(edges):
            edge = edges.pop(0)
            next_vertex = graph.getVertexIdx(edge.vertex2)
            weight = edge.weight

            if distance[next_vertex] > weight and intree[next_vertex] is False:
                distance[next_vertex] = weight
                parent[next_vertex] = current_vertex

        current_vertex = 0
        dist = float('inf')

        for i in range(graph.order()):
            if intree[i] is False and dist > distance[i]:
                dist = distance[i]
                next_vertex = i

        next_vertex_vertex = graph.getVertex(next_vertex)
        newGraph.insertVertex(next_vertex_vertex)

        parent_of_new_vertex = parent[next_vertex]

        new_edge = graph.adjList[parent_of_new_vertex][next_vertex_vertex]
        newGraph.insertEdge(new_edge.vertex1, new_edge.vertex2, new_edge.weight)

        current_vertex = next_vertex

    return newGraph


def main2():

    graph = AdjListGraph()

    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")

    vertices = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF]

    for vertex in vertices:
        graph.insertVertex(vertex)

    graph.insertEdge(vertexA, vertexB, 1)
    graph.insertEdge(vertexA, vertexD, 4)
    graph.insertEdge(vertexA, vertexE, 3)
    graph.insertEdge(vertexD, vertexB, 4)
    graph.insertEdge(vertexD, vertexE, 4)
    graph.insertEdge(vertexB, vertexE, 2)
    graph.insertEdge(vertexE, vertexC, 4)
    graph.insertEdge(vertexE, vertexF, 7)
    graph.insertEdge(vertexF, vertexC, 5)

    minimalGraph = prim_algorithm(graph, 0)

    print(minimalGraph.edges())

def main():
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

    firstGraph = AdjListGraph()

    for edge in graf:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])

        firstGraph.insertVertex(vertex1)
        firstGraph.insertVertex(vertex2)
        firstGraph.insertEdge(vertex1, vertex2, edge[2])

    minimalGraph = prim_algorithm(firstGraph, 0)

    printGraph(minimalGraph)

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(j, w, end=";")
        print()
    print("-------------------") 

main()
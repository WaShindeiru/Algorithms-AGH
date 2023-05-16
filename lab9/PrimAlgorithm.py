import matrix

def prim_algorithm(graph: AdjListGraph, start):

    newGraph = AdjListGraph()
    
    intree = [None for i in range(graph.order())]
    distance = [float('inf') for i in range(graph.order())]
    parent = [-1 for i in range(graph.order())]

    distance[start] = 0
    current_vertex = start

    newGraph.insertVertex(graph.getVertexIdx(current_vertex))

    while(intree[current_vertex] == False):

        intree[current_vertex] = True
        edges = graph.neighbourEdgesIdx(current_edge)

        while(edges):
            edge = edges.pop(0)
            next_vertex = graph.getVertexIdx(edge.vertex2)
            weight = edge.weight

            if distance[next_vertex] > weight and intree[next_vertex] is False:
                distance[next_vertex] = weight
                parent[next_vertex] = current_vertex

        current_vertex = 0
        dist = int('float')

        for i in range(graph.order()):
            if intree[i] is False and dist > distance[i]:
                dist = distance[i]
                next_vertex = i

        newGraph.insertVertex(graph.getVertexIdx(next_vertex))
        next_vertex_vertex = graph.getVertexIdx(next_vertex)
        newGraph.insertVertex(next_vertex)
        new_edge = graph.adjList[current_vertex][next_vertex_vertex]
        newGraph.insertEdge(new_edge.vertex1, new_edge.vertex2, new_edge.weight)

        current_vertex = next_vertex
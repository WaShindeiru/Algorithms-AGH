from graph import *

def bfs(graph: AdjListGraph, parent: list):

    visited = [False for x in range(graph.size())]
    queue = list()

    queue.append(graph.getVertexIdx(graph.source))
    visited[graph.getVertexIdx(graph.source)] = True

    while queue:
        VertexId = queue.pop()

        neighbours = graph.neighbours(VertexId)

        for newVertex, newEdge in neighbours:
            newVertexId = graph.getVertexIdx(newVertex)

            if visited[newVertexId] == False and newEdge.residual > 0:
                queue.append(newVertexId)
                parent[newVertexId] = VertexId
                visited[newVertexId] = True

                if newVertex == graph.sink:
                    return True

    return False

def FordFulkerson(graph: AdjListGraph) -> int:

    parent = [-1 for x in range(graph.size())]
    max_flow = 0

    while bfs(graph, parent):

        min_flow = float('inf')
        temp = graph.sink
        tempId = graph.getVertexIdx(temp)

        while temp != graph.source:
            edge = graph.adjList[parent[tempId]][temp]
            min_flow = min(min_flow, edge.residual)

            tempId = parent[tempId]
            temp = graph.getVertex(tempId)

        max_flow += min_flow

        temp = graph.sink
        tempId = graph.getVertexIdx(temp)

        while temp != graph.source:
            parentVertexId = parent[tempId]
            parentVertex = graph.getVertex(parentVertexId)

            graph.adjList[parentVertexId][temp].flow += min_flow
            graph.adjList[parentVertexId][temp].residual -= min_flow
            graph.adjList[tempId][parentVertex].flow -= min_flow
            graph.adjList[tempId][parentVertex].residual += min_flow

            tempId = parentVertexId
            temp = parentVertex

    return max_flow

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

def solve(graph):
    graph = AdjListGraph(graph)
    graph.setSink(Vertex("t"))
    graph.setSource(Vertex("s"))

    print(FordFulkerson(graph))
    printGraph(graph)


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    graphs = [graf_0, graf_1, graf_2, graf_3]

    for graph in graphs:
        solve(graph)


main()
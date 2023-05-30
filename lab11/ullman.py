from copy import deepcopy
from matrix import AdjMatrixGraph
import numpy as np

def ullman(current_row, matrix, used_columns, P, G, isomorphism):
    global ullman1_recursion_count
    global ullman1_matrix_count

    ullman1_recursion_count += 1
    if current_row == matrix.shape[0]:
        # print(matrix)
        if np.all(P == matrix.dot(np.transpose(matrix.dot(G)))):
            ullman1_matrix_count += 1
            isomorphism.append(matrix)

        return True

    matrix_copy = deepcopy(matrix)

    for i in range(len(used_columns)):
        if not used_columns[i]:
            used_columns[i] = True
            matrix_copy[current_row, :] = 0
            matrix_copy[current_row, i] = 1
            ullman(current_row+1, matrix_copy, used_columns, P, G, isomorphism)
            used_columns[i] = False

def ullman2(current_row, matrix, used_columns, P, G, isomorphism, M0):
    global ullman2_recursion_count
    global ullman2_matrix_count

    ullman2_recursion_count += 1
    if current_row == matrix.shape[0]:
        if np.all(P == matrix.dot(np.transpose(matrix.dot(G)))):
            ullman2_matrix_count += 1
            isomorphism.append(matrix)

        return True

    matrix_copy = deepcopy(matrix)

    for i in range(len(used_columns)):
        if not used_columns[i]:
            if M0[current_row][i] == 1:
                used_columns[i] = True
                matrix_copy[current_row, :] = 0
                matrix_copy[current_row, i] = 1
                ullman2(current_row+1, matrix_copy, used_columns, P, G, isomorphism, M0)
                used_columns[i] = False

def prune(M, G, P):
    change = True

    while change:
        change = False
        indices = np.where(M == 1)
        for i in range(len(indices[0])):
            if change:
                break

            x = indices[0][i]
            y = indices[1][i]

            p_neighbours = np.where(P[x] == 1)[0]
            g_neighbours = np.where(G[y] == 1)[0]

            for p_neighbour in p_neighbours:
                for g_neighbour in g_neighbours:
                    if M[p_neighbour, g_neighbour] == 1:
                        break
                else:
                    change = True
                    M[x, y] = 0
                    break

def ullman3(current_row, matrix, used_columns, P, G, isomorphism, M0):
    global ullman3_recursion_count
    global ullman3_matrix_count

    ullman3_recursion_count += 1
    if current_row == matrix.shape[0]:
        if np.all(P == matrix.dot(np.transpose(matrix.dot(G)))):
            ullman3_matrix_count += 1
            isomorphism.append(matrix)

        return True

    matrix_copy = deepcopy(matrix)
    prune(matrix_copy, G, P)

    for i in range(len(used_columns)):
        if not used_columns[i]:
            if M0[current_row][i] == 1:
                used_columns[i] = True
                matrix_copy[current_row, :] = 0
                matrix_copy[current_row, i] = 1
                ullman3(current_row+1, matrix_copy, used_columns, P, G, isomorphism, M0)
                used_columns[i] = False

if __name__ == "__main__":
    G_Graph = AdjMatrixGraph( [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)])
    P_Graph = AdjMatrixGraph( [ ('A','B',1), ('B','C',1), ('A','C',1)])

    G = G_Graph.toNumpyArray()
    P = P_Graph.toNumpyArray()

    example = np.zeros((3, 6))
    example2 = deepcopy(example)
    example3 = deepcopy(example)
    used_columns = [False for x in range(example.shape[1])]
    used_columns2 = deepcopy(used_columns)

    ullman1_recursion_count = 0
    ullman1_matrix_count = 0
    ullman1_isomorphism = list()
    ullman(0, example, used_columns, P, G, ullman1_isomorphism)
    print(ullman1_matrix_count, ullman1_recursion_count)

    ullman2_recursion_count = 0
    ullman2_matrix_count = 0
    ullman2_isomorphism = list()

    M0 = np.zeros((3, 6))

    for x in range(len(G)):
        G_sum = np.sum(G[x, :])
        for y in range(len(P)):
            P_sum = np.sum(P[y, :])
            if P_sum <= G_sum:
                M0[y, x] = 1

    M0_copy = deepcopy(M0)
    used_columns3 = deepcopy(used_columns2)

    ullman2(0, example2, used_columns2, P, G, ullman2_isomorphism, M0)
    print(ullman2_matrix_count, ullman2_recursion_count)

    ullman3_recursion_count = 0
    ullman3_matrix_count = 0
    ullman3_isomorphism = list()

    ullman3(0, example3, used_columns3, P, G, ullman3_isomorphism, M0_copy)
    print(ullman3_matrix_count, ullman3_recursion_count)
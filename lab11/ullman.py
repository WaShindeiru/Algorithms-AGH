from copy import deepcopy
import numpy as np

def ullman(current_row, matrix, used_columns):
    if current_row == matrix.shape[0]-1:
        print(matrix)
        return

    matrix_copy = deepcopy(matrix)

    for i in range(len(used_columns)):
        if not used_columns[i]:
            used_columns[i] = True
            matrix_copy[current_row, :] = 0
            matrix_copy[current_row, i] = 1
            ullman(current_row+1, matrix_copy, used_columns)
            used_columns[i] = False

def main():
    example = np.random.randint(2, size=(2, 3))
    used_columns = [False for x in range(example.shape[1])]

    ullman(0, example, used_columns)

main()
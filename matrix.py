# Franciszek Data
# Skończone

import copy

class matrix:
    def __init__(self, matrix_size, number = 0):
        if isinstance(matrix_size, tuple):
            self.__matrix_data = [[number] * matrix_size[1] for  i in range(matrix_size[0])]
            self.__sizey = matrix_size[0]
            self.__sizex = matrix_size[1]
        
        else:
            self.__matrix_data = copy.deepcopy(matrix_size)
            self.__sizey = len(matrix_size)
            self.__sizex = len(matrix_size[0])

    def size(self):
        return (self.__sizey, self.__sizex)

    def __add__(self, matrix_add):
        if not isinstance(matrix_add, matrix) or self.size() != matrix_add.size():
            raise Exception("Wrong shape")

        temp = copy.deepcopy(self.__matrix_data[:][:])
        for i in range(self.__sizey):
            for n in range(self.__sizex):
                temp[i][n] += matrix_add[i][n]
        
        return matrix(temp)
    
    def __getitem__(self, pos):
        return self.__matrix_data[pos]
    
    def __setitem__(self, pos, value):
        self.__matrix_data[pos] = value
        
    def __repr__(self):
        str = ""
        for i in range(len(self.__matrix_data)):
            str += self.__matrix_data[i].__repr__() 
            str += "\n"
        return str

    def __mul__(self, matrixb):
        if not isinstance(matrixb, matrix) or matrixb.size()[0] != self.size()[1]:
            raise Exception("Wrong shape")

        temp = [[0] * matrixb.size()[1] for i in range(self.__sizey)]
        for y in range(self.__sizey):
            for x in range(matrixb.size()[1]):
                for i in range(self.__sizex):
                    temp[y][x] += self.__matrix_data[y][i] * matrixb[i][x]

        return matrix(temp)

def transponse(mat: matrix):
    temp = matrix((mat.size()[1], mat.size()[0]))
    for y in range(mat.size()[0]):
        for x in range(mat.size()[1]):
            temp[x][y] = mat[y][x]

    return temp


def main():
    test = matrix([[1, 0, 2], [-1, 3, 1]])
    print(transponse(test))
    print(test + matrix((2, 3), 1))
    print(test * matrix([[3, 1], [2, 1], [1, 0]]))

if __name__ == "__main__":
    main()

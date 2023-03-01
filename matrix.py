import copy

class matrix:
    def __init__(self, matrix_size, number = 0):
        if isinstance(matrix_size, tuple):
            self.__matrix_data = [list()] * matrix_size[0]
            for i in range(matrix_size[0]):
                self.__matrix_data[i] = [number] * matrix_size[1]
            self.__sizey = matrix_size[0]
            self.__sizex = matrix_size[1]
        
        else:
            self.__matrix_data = copy.deepcopy(matrix_size)
            self.__sizey = len(matrix_size)
            self.__sizex = len(matrix_size[0])

    def size(self):
        return (self.__sizey, self.__sizex)

    def __add__(self, matrix_add):
        temp = self.__matrix_data[:][:]
        for i in range(self.__sizey):
            for n in range(self.__sizex):
                temp[i][n] += matrix_add[i, n]
        
        return matrix(temp)
    
    def __getitem__(self, pos):
        x, y = pos
        return self.__matrix_data[x][y]
        

    def __repr__(self):
        str = ""
        for i in range(len(self.__matrix_data)):
            str += self.__matrix_data[i].__repr__() 
            str += "\n"
        return str


c = matrix([[2, 3], [4, 5]])
d = matrix((2, 2), 2)
print(c + d)

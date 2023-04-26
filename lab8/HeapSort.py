import random
import time
from SelectionSort import SelectionSort

class Node:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __repr__(self):
        return str(self.__priority) + ": " + str(self.__data)

    def __lt__(self, node):
        return self.__priority < node.__priority

    def __gt__(self, node):
        return self.__priority > node.__priority

    def Data(self):
        return self.__data

    def Priority(self):
        return self.__priority


class PriorityQueue:
    def __init__(self, data = None):
        if data is None:
            self.__data = list()
            self.size = 0

        self.size = len(data)
        self.__data = data

        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    @staticmethod
    def parent(i):
        return (i-1)//2

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    def heapify(self, i):
        left = PriorityQueue.left(i)
        right = PriorityQueue.right(i)

        largest = i
        if left < self.size and self.__data[left] > self.__data[i]:
            largest = left

        if right < self.size and self.__data[right] > self.__data[largest]:
            largest = right

        if largest != i:
            self.__data[i], self.__data[largest] = self.__data[largest], self.__data[i]
            self.heapify(largest)

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.size == 0:
            return None
        return self.__data[0]

    def dequeue(self):
        if self.size == 0:
            return None

        temp = self.__data[0]
        self.size -= 1

        self.__data[0], self.__data[self.size] = self.__data[self.size], self.__data[0]

        self.heapify(0)

        return temp

    def heapSort(self):
        while self.size > 1:
            self.dequeue()

        return self.__data[:]

    def enqueue(self, data, priority):
        if self.size == len(self.__data):
            self.__data.append(Node(data, priority))
        
        else:
            self.__data[self.size] = Node(data, priority)

        i = self.size

        while i > 0 and self.__data[PriorityQueue.parent(i)] < self.__data[i]:
            self.__data[PriorityQueue.parent(i)], self.__data[i] = self.__data[i], self.__data[PriorityQueue.parent(i)]
            i = PriorityQueue.parent(i)

        self.size += 1

    def print_tab(self):
        print ('{', end=' ')
        print(*self.__data[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx=0, lvl=0):
        if idx<self.size:           
            self.print_tree(PriorityQueue.right(idx), lvl+1)
            print(2*lvl*'  ', self.__data[idx] if self.__data[idx] else None)           
            self.print_tree(PriorityQueue.left(idx), lvl+1)

    @staticmethod
    def print_data(data):
        aha = ""
        for i in data:
            aha += str(i.Priority()) + " " + str(i.Data()) + ", "
        
        print(aha)

def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for i in range(len(data)):
        data[i] = Node(data[i][1], data[i][0])

    queue = PriorityQueue(data)
    queue.print_tab()
    queue.print_tree()

    queue.heapSort()
    print(data)

    print("Sortowanie nie jest stabilne")


    data2 = list()
    for i in range(1000):
        temp = int(random.random() * 100)
        data2.append(Node(temp, temp))

    t_start = time.perf_counter()

    queue2 = PriorityQueue(data2)
    queue2.heapSort()

    t_stop = time.perf_counter()

    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return(t_stop - t_start)

def main2():
    data =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for i in range(len(data)):
        data[i] = Node(data[i][1], data[i][0])
    
    SelectionSort(data)

    print(data)

    print("Sortowanie nie jest stabilne")

    data2 = list()
    for i in range(100):
        temp = int(random.random() * 100)
        data2.append(Node(temp, temp)) 

    t_start = time.perf_counter()

    SelectionSort(data2)

    t_stop = time.perf_counter()

    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return(t_stop - t_start)

if __name__ == "__main__":
    time1 = main()
    time2 = main2()

    print("Sortowanie kopcowe, czas: {}".format(time1))
    print("Sortowanie przez wybieranie: {}".format(time2))

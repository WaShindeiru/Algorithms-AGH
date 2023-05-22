from InsertionSort import InsertionSort
from HeapSort import PriorityQueue
import random
import time

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


def ShellSort(tab):
    
    array = tab[:]
    size = len(array)
    interval = size//2

    while(interval > 0):
        for i in range(interval, size):
            
            key = array[i]
            j = i - interval
            while j>=0 and array[j] > key:
                array[j], array[j+interval] = array[j+interval], array[j]   
                j -= interval

        interval = interval // 2

    return array

def main():

    array_to_sort = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    list_to_sort = [Node(x[1], x[0]) for x in array_to_sort]
    
    print("Algorytm Shella: ")
    print(ShellSort(list_to_sort))
    print("Algorytm Shella nie jest stabilny")
    print()

    print("Sortowanie przez wstawianie: ")
    print(InsertionSort(list_to_sort))
    print("Algorytm jest stabilny")
    print()

    data2 = list()
    for i in range(10000):
        temp = int(random.random() * 100)
        data2.append(temp) 

    t_start_Shell = time.perf_counter()

    Random_Shell = ShellSort(data2)

    t_stop_Shell = time.perf_counter()
    time_Shell = t_stop_Shell - t_start_Shell

    t_start_Insertion = time.perf_counter()
    Random_Insertion = InsertionSort(data2)
    t_stop_Insertion = time.perf_counter()
    time_Insertion = t_stop_Insertion - t_start_Insertion

    t_start_heap = time.perf_counter()

    queue2 = PriorityQueue(data2)
    Random_Heap = queue2.heapSort()

    t_stop_heap = time.perf_counter()
    heap_time = t_stop_heap - t_start_heap

    print("Algorytm Shella: ")
    print("Czas: {}".format(time_Shell))

    print("Sortowanie przez wstawianie: ")
    print("Czas: {}".format(time_Insertion))

    print("Sortowanie kopcowe")
    print("Czas: {}".format(heap_time))

if __name__ == "__main__":
    main()
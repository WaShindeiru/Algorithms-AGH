class Node:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __str__(self):
        return str(self.__priority) + ": " + str(self.__data)

    def __lt__(self, node):
        return self.__priority < node.__priority

    def __gt__(self, node):
        return self.__priority > node.__priority

    def Data(self):
        return self.__data


class PriorityQueue:
    def __init__(self):
        self.__data = list()
        self.size = 0

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
        return self.__data[0].Data()

    def dequeue(self):
        if self.size == 0:
            return None

        temp = self.__data[0].Data()

        self.__data[0] = self.__data[self.size - 1]
        self.size -= 1

        self.heapify(0)

        return temp

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

def main():
    queue = PriorityQueue()

    for number, leter in zip([7, 5, 1, 2, 5, 3, 4, 8, 9], "GRYMOTYLA"):
        queue.enqueue(leter, number)

    queue.print_tree(0, 0)
    queue.print_tab()

    temp = queue.dequeue()
    print(queue.peek())

    queue.print_tab()
    print(temp)

    while(not queue.is_empty()):
        print(queue.dequeue())

    queue.print_tab()

if __name__ == "__main__":
    main()
import copy

class CyclicQueue:
    def __init__(self):
        self.size = 5
        self.queue = [None for i in range(self.size)]
        self.read = 0
        self.write = 0

    @staticmethod
    def realloc(tab, size):
        oldSize = len(tab)
        return [tab[i] if i<oldSize else None for i in range(size)]
    
    def is_empty(self):
        return self.read == self.write

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.read]
    
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[self.read]
        self.read = (self.read + 1)%self.size
        return data
    
    def enqueue(self, data):
        self.queue[self.write] = data
        self.write = (self.write + 1)%self.size

        if self.read == self.write:
            newQueue = self.realloc(self.queue, self.size*2)
            newWrite = 0
            for i in range(0, self.read):
                newWrite = self.size + i
                newQueue[newWrite] = self.queue[i]
                
            self.size = self.size * 2
            self.write = (newWrite + 1)%self.size
            self.queue = newQueue

    def __str__(self):
        if self.is_empty():
            return ""
        QueueString = "["
        if self.write < self.read:
            for i in range(self.read, self.size):
                QueueString += str(self.queue[i]) + ", "
            for i in range(0, self.write):
                QueueString += str(self.queue[i])
                if i < self.write - 1:
                    QueueString += ", "
                else:
                    QueueString += "]"

        else:
            for i in range(self.read, self.write, 1):
                QueueString += str(self.queue[i])
                if i < self.write - 1:
                    QueueString += ", "
                else:
                    QueueString += "]"

        return QueueString
    
    def write_table(self):
        aha = ""
        for i in self.queue:
            aha += str(i) + ", "
        return aha

def main():          
    example = CyclicQueue()
    for i in range(1, 5):
        example.enqueue(i)

    print(example.dequeue())
    print(example.peek())
    print(example)

    for i in range(5, 9):
        example.enqueue(i)

    print(example.write_table())

    while(not example.is_empty()):
        print(example.dequeue())

    print(example)

if __name__ == "__main__":
    main()
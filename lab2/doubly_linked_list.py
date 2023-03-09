class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add(self, data):
        if self._head is None:
            self._head = Node(data, None, None)
            self._tail = self._head
        else:
            self._head.prev = Node(data, self._head, None)
            self._head = self._head.prev
            

    def append(self, data):
        if self._tail is None:
            self._tail = Node(data, None, None)
            self._head = self._tail
        temp = Node(data, None, self._tail)
        self._tail.next = temp
        self._tail = temp

    def remove(self):
        self.head = self.head.next
        self.head.prev = None

    def length(self):
        if self._head is None:
            return 0
        temp = self._head
        i = 1
        while(temp.next != None):
            temp = temp.next
            i += 1
        return i
    
    def is_empty(self):
        return self.length() == 0

    def __str__(self):
        if self.is_empty():
            return "Empty"
        temp = self._head
        repr = ""
        while(temp.next != None):
            repr += "->"
            repr += str(temp.data)
            repr += "\n"
            temp = temp.next
        repr += "->"
        repr += str(temp.data)
        return repr

example = DoublyLinkedList()
example.add(1)
example.append(10)
example.add(5)
example.append(55)
print(example)

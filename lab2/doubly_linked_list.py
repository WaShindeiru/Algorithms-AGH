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
        else:
            temp = Node(data, None, self._tail)
            self._tail.next = temp
            self._tail = temp

    def remove(self):
        if self._head is None:
            pass
        elif self._head.next is None:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

    def remove_end(self):
        if self._tail is None:
            pass
        elif self._tail.prev is None:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

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

    def get(self):
        if self._head is None:
            return None
        return self._head.data

    def destroy(self):
        if self._head is None:
            pass
        temp = self._head
        while(not temp.next is None):
            temp = temp.next
            temp.prev.next = None
            temp.prev = None
        self._head = None
        self._tail = None

def main():
    uczelnie = DoublyLinkedList()
    uczelnie.append(('AGH', 'Kraków', 1919))
    uczelnie.append(('UJ', 'Kraków', 1364))
    uczelnie.append(('PW', 'Warszawa', 1915))
    uczelnie.add(('UW', 'Warszawa', 1915))
    uczelnie.add(('UP', 'Poznań', 1919))
    uczelnie.add(('PG', 'Gdańsk', 1945))

    print(uczelnie)

    print("Długość listy {}".format(uczelnie.length()))
    uczelnie.remove()
    print("Pierwszy element: {}".format(uczelnie.get()))
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    uczelnie.remove()
    uczelnie.remove_end()

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def destroy(self):
        self._head = None

    def add(self, data):
        new = Node(data, self._head)
        self._head = new
    
    def length(self):
        if self._head is None:
            return 0
        temp = self._head
        i = 1
        while(temp.next != None):
            temp = temp.next
            i += 1
        return i
    
    def append(self, data):
        if self._head is None:
            self._head = Node(data, None)
        else:
            temp = self._head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(data, None)

    def is_empty(self):
        return self.length() == 0
    
    def get(self):
        if self._head == None:
            return None
        return self._head.data
    
    def remove_end(self):
        if self._head == None:
            pass
        elif self._head.next == None:
            self._head = None
        else:
            temp = self._head
            while(temp.next != None):
                previous = temp
                temp = temp.next
            previous.next = None

    def remove(self):
        if self._head == None:
            pass
        elif self._head.next == None:
            self._head = None
        else:
            self._head = self._head.next

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


def main():
    uczelnie = LinkedList()
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

main()

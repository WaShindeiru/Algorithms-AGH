class Entry:
    def __init__(self, key, data):
        self.key = key
        self.data = data

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def computeHash(self, number, i):
        if isinstance(number, float) or isinstance(number, int):
            return (number + self.c1*i + self.c2*i*i)%self.size
        elif isinstance(number, str):
            sum = 0
            for a in number:
                sum += ord(a)
            return (sum + self.c1*i + self.c2*i*i)%self.size

    def search(self, key):
        value = hash = self.computeHash(key, 0)
        i = 0
        
        while True:
            if self.tab[value] == None:
                return None
            elif self.tab[value].key == key:
                return self.tab[value].data
            
            i += 1
            value = self.computeHash(key, i)
            if value == hash:
                return None

    def insert(self, key, data):
        value = hash = self.computeHash(key, 0)
        i = 0
        
        while True:
            if self.tab[value] == None or self.tab[value].key == None:
                self.tab[value] = Entry(key, data)
                return data
            elif self.tab[value].key == key:
                temp = self.tab[value].data
                self.tab[value] = Entry(key, data)
                return temp
            
            i += 1
            value = self.computeHash(key, i)
            if value == hash:
                return None

    def remove(self, key):
        value = hash = self.computeHash(key, 0)
        i = 0

        while True:
            if self.tab[value] == None:
                return value
            elif self.tab[value].key == key:
                self.tab[value].key = None
                self.tab[value].data = None
                return value

            i += 1
            value = self.computeHash(key, i)
            if value == hash:
                return None


    def __str__(self):
        text = "{"
        for i in range(self.size):
            if self.tab[i] == None:
                text += "None"
            else:
                text += (str(self.tab[i].key) + ":" + str(self.tab[i].data))
            if i == self.size - 1:
                text += "}"
            else:
                text += ", "

        return text

def table_search(key, table):
    data = table.search(key)
    if data == None:
        print("Brak danej")
    else:
        print(data)

def main1():
    table = HashTable(13)
    table.insert("test", "W")
    for index, letter in enumerate("ABCDEFGHIJKLMNO"):
        index += 1
        if index == 6:
            table.insert(18, letter)
        elif index == 7:
            table.insert(31, letter)
        else:
            table.insert(index, letter)

    print(table)  

    table_search(5, table)

    table_search(14, table) 

    table.insert(5, "Z")
    table_search(5, table)
    
    table.remove(5)
    print(table)

    table.search(31)

def main2():
    table = HashTable(13)
    for index, letter in enumerate("ABCDEFGHIJKLMNO"):
        index += 1
        if index == 6:
            table.insert(18, letter)
        elif index == 7:
            table.insert(31, letter)
        else:
            table.insert(index*13, letter)

    print(table)  

def main3():
    table = HashTable(13, 0, 1)
    for index, letter in enumerate("ABCDEFGHIJKLMNO"):
        index += 1
        if index == 6:
            table.insert(18, letter)
        elif index == 7:
            table.insert(31, letter)
        else:
            table.insert(index, letter)

    print(table)

def test():
    table = HashTable(13)
    table.insert(5, "aha")
    table.insert(18, "super")
    print(table)

    table.remove(5)
    print(table)
    print(table.search(18))

if __name__ == "__main__":
    test()

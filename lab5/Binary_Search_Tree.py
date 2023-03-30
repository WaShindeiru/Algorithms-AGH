class Node:
    def __init__(self, key, data, left, right):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def create(key, value):
        return Node(key, value, None, None)

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def search(self, key):
        return self.search_recursive(self.root, None, key)[0]

    def search_recursive(self, node, previous, key):
        if node == None:
            return None

        if key == node.key:
            return node, previous

        if key < node.key:
            return self.search_recursive(node.left, node, key)

        else:
            return self.search_recursive(node.right, node, key)

    def insert(self, key, value):
        self.insert_recursive(Node.create(key, value), self.root, None)

    def insert_recursive(self, node, current, previous):
        if current != None and current.key != node.key:
            previous = current
            if node.key < current.key:
                current = current.left
            
            else:
                current = current.right
            self.insert_recursive(node, current, previous)

        elif previous == None:
            self.root = node

        elif current == None:
            if node.key < previous.key:
                previous.left = node

            else:
                previous.right = node

        elif current.key == node.key:
            node.left = current.left
            node.right = current.right
            
            if node.key < previous.key:
                prvious.left = node
            
            else:
                previous.right = node

            current.left = None
            current.right = None

    def height(self) -> int:
        return self.height_recursive(self.root)

    def height_recursive(self, node: Node) -> int:
        if node is None:
            return 0
        leftHeight = self.height_recursive(node.left)
        rightHeight = self.height_recursive(node.right)
        return max(leftHeight, rightHeight) + 1

    def find_min(self, node):
        while node.left != None:
            node = node.left

        return node

    def find_max(self, node):
        while node.right != None:
            node = node.right

        return node

    def min_walk(self):
        self.walk_recursive(self.root)
        print()

    def walk_recursive(self, node):
        if node != None:
            self.walk_recursive(node.left)
            print(node.key, node.data, sep=" ",end=",")    
            self.walk_recursive(node.right)

    def transplant(self, old: Node, parent: Node, new: Node):
        if parent is None:
            self.root = new

        elif parent.left == old:
            parent.left = new
        
        else:
            parent.right = new

    def delete(self, key):
        z, parent = self.search_recursive(self.root, None, key)

        if z.left is None:
            self.transplant(z, parent, z.right)

        elif z.right is None:
            self.transplant(z, parent, z.left)

        else:
            temp = z.right
            previous = None

            while temp.left != None:
                previous = temp
                temp = temp.left

            if z.right != temp:
                self.transplant(temp, previous, temp.right)
                temp.right = z.right
            self.transplant(z, parent, temp)
            temp.left = z.left
        

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)

def main():
    aha = BinarySearchTree(root=Node(50, "A", None, None))
    aha.insert(15, "B")
    aha.insert(62, "C")
    aha.insert(5, "D")
    aha.insert(20, "E")
    aha.insert(58, "F")
    aha.insert(91, "G")
    aha.insert(3, "H")
    aha.insert(8, "I")
    aha.insert(37, "J")
    aha.insert(60, "K")
    aha.insert(24, "L")

    aha.print_tree()
    aha.min_walk()

    data_if_not_null = lambda x: x.data if x != None else ""

    print(data_if_not_null(aha.search(24)))
    aha.insert(20, "AA")
    aha.insert(6, "M")
    aha.delete(62)
    aha.insert(59, "N")
    aha.insert(100, "P")
    aha.delete(8)
    aha.delete(15)
    aha.insert(55, "R")
    aha.delete(50)
    aha.delete(5)
    aha.delete(24)
    print(aha.height())
    aha.min_walk()

    aha.print_tree()

                
if __name__ == "__main__":
    main()
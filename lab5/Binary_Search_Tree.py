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
        return search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node == None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return search_recursive(node.left, key)

        else:
            return search_recursive(node.right, key)

    def insert(self, node):
        self.insert_recursive(node, self.root, Node)

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
    aha = BinarySearchTree(root=Node(2, "aha", None, None))
    aha.insert(Node.create(50, "A"))
    aha.insert(Node.create(15, "B"))
    aha.insert(Node.create(62, "C"))
    aha.insert(Node.create(5, "D"))
    aha.insert(Node.create(20, "E"))
    aha.insert(Node.create(58, "F"))
    aha.insert(Node.create(91, "G"))
    aha.insert(Node.create(91, "BO"))

    aha.print_tree()
                
if __name__ == "__main__":
    main()
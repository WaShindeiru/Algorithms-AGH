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
        self.root = self.insert_recursive(key, value, self.root)

    def insert_recursive(self, key, data, node):

        if node == None:
            node = Node(key, data, None, None)

        elif node.key == key:
            node.data = data

        elif key < node.key:
            node.left = self.insert_recursive(key, data, node.left)

        else:
            node.right = self.insert_recursive(key, data, node.right)

        return node

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

    def print(self):
        self.walk_recursive(self.root)
        print()

    def walk_recursive(self, node):
        if node != None:
            self.walk_recursive(node.left)
            print(node.key, node.data, sep=" ",end=",")    
            self.walk_recursive(node.right)

    def delete(self, key):
        self.root = self.delete_recursively(key, self.root)

    def delete_recursively(self, key, node):
        if node == None:
            return None
        
        if key < node.key:
            node.left = self.delete_recursively(key, node.left)

        elif key > node.key:
            node.right = self.delete_recursively(key, node.right)

        else:
            if node.left is None:
                rightChild = node.right

                node.key = None
                node.data = None
                node = None

                return rightChild

            if node.right is None:
                leftChild = node.left

                node.data = None
                node.key = None
                node = None

                return leftChild

            else:
                temp = self.find_min(node.right)

                node.data = temp.data
                node.key = temp.key

                node.right = self.delete_recursively(temp.key, node.right)

        return node

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
    tree = BinarySearchTree(root=Node(50, "A", None, None))
    tree.insert(15, "B")
    tree.insert(62, "C")
    tree.insert(5, "D")
    tree.insert(20, "E")
    tree.insert(58, "F")
    tree.insert(91, "G")
    tree.insert(3, "H")
    tree.insert(8, "I")
    tree.insert(37, "J")
    tree.insert(60, "K")
    tree.insert(24, "L")

    tree.print_tree()
    tree.print()

    data_if_not_null = lambda x: x.data if x != None else ""

    print(data_if_not_null(tree.search(24)))
    tree.insert(20, "AA")
    tree.insert(6, "M")
    tree.delete(62)
    tree.insert(59, "N")
    tree.insert(100, "P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, "R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()

    tree.print_tree()

                
if __name__ == "__main__":
    main()
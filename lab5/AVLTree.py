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
        return self.height_recursive(self.root) - 1

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
            print(node.key, node.data, sep=": ",end=",")    
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

class AVLNode(Node):
    def __init__(self, key, data, left=None, right=None, height=0):
        super().__init__(key, data, left, right)
        self.height = height

    @staticmethod
    def getHeight(node):
        if node is None:
            return -1
        
        return node.height

    @staticmethod
    def getBalance(node):
        if node is None:
            return 0

        return AVLNode.getHeight(node.left) - AVLNode.getHeight(node.right)

class AVLTree(BinarySearchTree):

    def insert_recursive(self, key, data, node):
        if node is None:
            node = AVLNode(key, data, None, None)

        elif node.key == key:
            node.data = data

        elif key < node.key:
            node.left = self.insert_recursive(key, data, node.left)

        else:
            node.right = self.insert_recursive(key, data, node.right)

        node.height = 1 + max(AVLNode.getHeight(node.left), AVLNode.getHeight(node.right))
        balanceFactor = AVLNode.getBalance(node)

        if balanceFactor > 1 and key < node.left.key:
            return AVLTree.rotateRight(node)

        if balanceFactor < -1 and key > node.right.key:
            return AVLTree.rotateLeft(node)

        if balanceFactor > 1 and key > node.left.key:
            node.left = AVLTree.rotateLeft(node.left)
            return AVLTree.rotateRight(node)

        if balanceFactor < -1 and key < node.right.key:
            node.right = AVLTree.rotateRight(node.right)
            return AVLTree.rotateLeft(node)

        return node

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

        node.height = 1 + max(AVLNode.getHeight(node.left), AVLNode.getHeight(node.right))
        balanceFactor = AVLNode.getBalance(node)

        if balanceFactor > 1 and AVLNode.getBalance(node.left) >= 0:
            return AVLTree.rotateRight(node)

        if balanceFactor < -1 and AVLNode.getBalance(node.right) <= 0:
            return AVLTree.rotateLeft(node)

        if balanceFactor > 1 and AVLNode.getBalance(node.left) < 0:
            node.left = AVLTree.rotateLeft(node.left)
            return AVLTree.rotateRight(node)

        if balanceFactor < -1 and AVLNode.getBalance(node.right) > 0:
            node.right = AVLTree.rotateRight(node.right)
            return AVLTree.rotateLeft(node)

        return node

    @staticmethod
    def rotateRight(z: AVLNode) -> AVLNode:
        leftchild = z.left
        temp = leftchild.right

        leftchild.right = z
        z.left = temp

        z.height = 1 + max(AVLNode.getHeight(z.left), AVLNode.getHeight(z.right))
        leftchild.height = 1 + max(AVLNode.getHeight(leftchild.left), AVLNode.getHeight(leftchild.right))

        return leftchild

    @staticmethod
    def rotateLeft(z: AVLNode) -> AVLNode:
        rightchild = z.right
        temp = rightchild.left

        rightchild.left = z
        z.right = temp

        z.height = 1 + max(AVLNode.getHeight(z.left), AVLNode.getHeight(z.right))
        rightchild.height = 1 + max(AVLNode.getHeight(rightchild.left), AVLNode.getHeight(rightchild.right))

        return rightchild

def main():
    data_if_not_null = lambda x: x.data if x != None else ""

    tree = AVLTree(root=AVLNode(50, "A", None, None, 0))
    tree.insert(15, "B")
    tree.insert(62, "C")
    tree.insert(5, "D")
    tree.insert(2, "E")
    tree.insert(1, "F")
    tree.insert(11, "G")
    tree.insert(100, "H")
    tree.insert(7, "I")
    tree.insert(6, "J")
    tree.insert(55, "K")
    tree.insert(52, "L")
    tree.insert(51, "M")
    tree.insert(57, "N")
    tree.insert(8, "O")
    tree.insert(9, "P")
    tree.insert(10, "R")
    tree.insert(99, "S")
    tree.insert(12, "T")

    tree.print_tree()
    tree.print()

    print(data_if_not_null(tree.search(10)))
    tree.delete(50)
    tree.delete(52)
    tree.delete(11)
    tree.delete(57)
    tree.delete(1)
    tree.delete(12)
    tree.insert(3, "AA")
    tree.insert(4, "BB")
    tree.delete(7)
    tree.delete(8)

    tree.print_tree()
    tree.print()

                
if __name__ == "__main__":
    main()
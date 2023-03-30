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
    tree.min_walk()

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
    tree.min_walk()

    tree.print_tree()

                
if __name__ == "__main__":
    main()
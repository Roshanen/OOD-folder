class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.value)

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, value):
        if (root is None):
            self.root = Node(value)
        else:
            if (root.value > value):
                if (root.left is None):
                    root.left = Node(value)
                else:
                    self.insert(root.left, value)
            else:
                if (root.right is None):
                    root.right = Node(value)
                else:
                    self.insert(root.right, value)

    def height(self, root):
        if (root is None):
            return -1
        return (max(self.height(root.left), self.height(root.right)) + 1)
    
    def inorder(self, root):
        if (root is not None):
            self.inorder(root.left)
            print(root, end=" ")
            self.inorder(root.right)
            
    def preorder(self, root):
        if (root is not None):
            print(root, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self, root):
        if (root is not None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root, end=" ")
            
    def levelorder(self, root):
        temp = []
        temp.append(root)
        while (len(temp) != 0):
            root = temp.pop(0)
            print(root, end=" ")
            if (root.left is not None):
                temp.append(root.left) 
            if (root.right is not None):
                temp.append(root.right) 

tree = Tree()
inp = [int(i) for i in input("Enter Input : ").split(" ")]
for item in inp:
    tree.insert(tree.root, item)
    
# print("Height of this tree is :", tree.height(tree.root))
# print("Preorder : ", end="")
# tree.preorder(tree.root)
# print("\nInorder : ", end="")
# tree.inorder(tree.root)
# print("\nPostorder : ", end="")
# tree.postorder(tree.root)
# print("\nBreadth : ", end="")
# tree.levelorder(tree.root)

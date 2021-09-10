class Node(object):
    def __init__(self, data):
        self.data = data
        self.lefttree = None
        self.righttree = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        
        
    def preorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._preorder(self.root)
            
            
    def _preorder(self, current):
        if current:
            print(current.data, end = " ")
            self._preorder(current.lefttree)
            self._preorder(current.righttree)
            
            
    def inorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._inorder(self.root)
            
            
    def _inorder(self, current):
        if current:
            self._inorder(current.lefttree)
            print(current.data, end = " ")
            self._inorder(current.righttree)
            
            
    def postorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._postorder(self.root)
            
            
    def _postorder(self, current):
        if current:
            self._postorder(current.lefttree)
            self._postorder(current.righttree)
            print(current.data, end = " ")
            
            
            
### BINARY TREE CODE IS COMPLETED... ###
# ob1 = BinaryTree()
# first = Node(54)
# second = Node(64)
# third = Node(44)
# fourth = Node(34)
# fifth = Node(24)
# sixth = Node(14)
# seventh = Node(4)
# ob1.root = first
# first.lefttree = second
# first.righttree = third
# second.lefttree = fourth
# second.righttree = fifth
# third.lefttree = sixth
# third.righttree = seventh
# print(first.lefttree.data)
# print()
# print("Preorder Data", end = " ")
# ob1.preorder()
# print()
# print("Inorder Data", end = " ")
# ob1.inorder()
# print()
# print("Postorder Data", end = " ")
# ob1.postorder()



### ................................... ###

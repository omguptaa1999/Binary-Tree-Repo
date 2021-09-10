class Node(object):
    def __init__(self, data):
        self.data = data
        self.lefttree = None
        self.righttree = None
        

class Binary_Search_Tree(object):
    def __init__(self):
        self.root = None
        
        
    def preorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._preorder(self.root)
            
    def _preorder(self, theia):
        if theia:
            print(theia.data, end = " ")
            self._preorder(theia.lefttree)
            self._preorder(theia.righttree)
            
            
    def inorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._inorder(self.root)
            
    def _inorder(self, theia):
        if theia:
            self._inorder(theia.lefttree)
            print(theia.data, end = " ")
            self._inorder(theia.righttree)
            
            
    def postorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            self._postorder(self.root)
            
    def _postorder(self, theia):
        if theia:
            self._postorder(theia.lefttree)
            self._postorder(theia.righttree)
            print(theia.data, end = " ")
            
            
    def addnode(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._addnode(self.root, val)
            
    def _addnode(self, theia, val):
        if theia.data > val:
            if theia.lefttree == None:
                theia.lefttree = Node(val)
            else:
                self._addnode(theia.lefttree, val)
                
        elif theia.data < val:
            if theia.righttree == None:
                theia.righttree = Node(val)
            else:
                self._addnode(theia.righttree, val)
                
        else:
            print("Value is Already Added!!!")
            
            
            
            
### BINARY SEARCH TREE CODE IS COMPLETED... ###



# ob1 = Binary_Search_Tree()
# ob1.addnode(48)
# ob1.addnode(8)
# ob1.addnode(36)
# ob1.addnode(6)
# ob1.addnode(16)
# print("Preorder Data", end = " ")
# ob1.preorder()
# print()
# print("Inorder Data", end = " ")
# ob1.inorder()
# print()
# print("Postorder Data", end = " ")
# ob1.postorder()



### ....................................... ###

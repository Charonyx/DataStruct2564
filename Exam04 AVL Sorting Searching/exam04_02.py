# Chapter : 16 - item : 2 - AVL Tree (บ่าย)

# เติมส่วนที่ขาดหายไปให้สมบูรณ์

# ห้ามแก้ไขส่วนอื่น

class Node:
    def __init__(self, data, left = None, right = None) :
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self) :
        return str(self.data)

class AVLTree:
    def __init__(self) :
        self.root = None

    def insert(self, data, node) :
        # if node == None : node = self.root

        # if not self.root :
        #     return Node(data)
        # else :
        if not node :
            return Node(data)
        if data < node.data :
            node.left = self.insert(data, node.left)
        else :
            node.right = self.insert(data, node.right)
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        
        bal = self.getBalance(node)

        if bal > 1 and data < node.left.data :
            return self.rightotate(node)

        if bal < -1 and data > node.right.data :
            return self.leftRotate(node)

        if bal > 1 and data > node.left.data :
            node.left = self.leftRotate(node.right)
            return self.rightotate(node)

        if bal < -1 and data < node.right.data :
            node.right = self.rightotate(node.left)
            return self.leftRotate(node)

        return node
    
    # def insert(self, data) :
    #     if not self.root :
    #         self.root = Node(data)
    #         return 
    #     else :
    #         node = self.root
    #         while node :
    #             if data < node.data :
    #                 if not node.left :
    #                     node.left = Node(data)
    #                     return self.root
    #                 node = node.left
    #             else :
    #                 if not node.right :
    #                     node.right = Node(data)
    #                     return self.root
    #                 node = node.right
        
    def leftRotate(self, z) :
        y = z.right
        t = y.left

        y.left = z
        z.right = t
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightotate(self, z) :
        y = z.left
        t = y.right

        y.right = z
        z.left = t
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def getHeight(self, node) :
        if not node :
            return 0
        return node.height

    def getBalance(self, node) :
        if not node :
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def preorder(self, node) :
        if node :
            _str = str(node) + ' ' + self.preorder(node.left) + self.preorder(node.right)
            return _str
        return ''

    def inorder(self, node) :
        if node :
            _str = self.inorder(node.left) + str(node) + ' ' + self.inorder(node.right)
            return _str
        return ''

    def postorder(self, node) :
        if node :
            _str = self.postorder(node.left) + self.postorder(node.right) + str(node) + ' '
            return _str
        return ''

    def print_preorder(self) :
        print(f'preorder  --> {self.preorder(self.root)}')

    def print_inorder(self) :
        print(f'in_order  --> {self.inorder(self.root)}')

    def print_postorder(self) :
        print(f'postorder --> {self.postorder(self.root)}')

    def printTree(self, node, l = 0) -> None :
        if node :
            self.printTree(node.right, l + 1)
            print('    ' * l, node.data)
            self.printTree(node.left, l + 1)

print(" *** AVL Tree ***")    

input_string = input("Enter some numbers : ")

bst = AVLTree()
root = None
for n in input_string.split():

    root = bst.insert(int(n), root)
    bst.printTree(root)
    print('TTTTTTTTTTTTT')

bst.print_inorder()
bst.print_preorder()
bst.print_postorder()


print(f'inorder {bst.inorder(bst.root)}')
print(f'preorder {bst.preorder(bst.root)}')
print(f'postorder {bst.postorder(bst.root)}')

'''
 *** AVL Tree ***
Enter some numbers : 1 2 3 4 5
in_order  --> 1 2 3 4 5 
preorder  --> 2 1 4 3 5 
postorder --> 1 3 5 4 2 
'''
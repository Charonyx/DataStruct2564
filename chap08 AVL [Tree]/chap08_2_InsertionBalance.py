# Title       : Chapter : 8 - item : 2 - ALV insert
# Question    : ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert ให้ตรวจสอบว่า balance หรือยัง หากไม่ให้ ปรับ Balance ให้เรียบร้อยแล้วและแสดงผล
# ** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self) :
        self.root = None

    # def insert(self, data) :
    #     _new = TreeNode(data)
    #     if self.root == None :
    #         self.root = _new
    #     else :
    #         _node = self.root
    #         while _node != None :
    #             if data < _node.val :
    #                 if _node.left == None :
    #                     _node.left = _new
    #                     break
    #                 _node = _node.left
    #             else :
    #                 if _node.right == None :
    #                     _node.right = _new
    #                     break
    #                 _node = _node.right

    def insert(self, node, data):
        if not node:
            # print('eiei')
            return TreeNode(data)
        elif data < node.val:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
 
        # Height (Ancestor node)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        # Balance factor
        balance = self.getBalance(node)

        # Rebalanced : Case 1 - Left Left
        if balance > 1 and data < node.left.val:
            print('Not Balance, Rebalance!')
            return self.rightRotate(node)
 
        # Rebalanced : Case 2 - Right Right
        if balance < -1 and data > node.right.val:
            print('Not Balance, Rebalance!')
            return self.leftRotate(node)
 
        # Rebalanced : Case 3 - Left Right
        if balance > 1 and data > node.left.val:
            print('Not Balance, Rebalance!')
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
 
        # Rebalanced : Case 4 - Right Left
        if balance < -1 and data < node.right.val:
            print('Not Balance, Rebalance!')
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
 
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")

'''
Enter Input : 50 40 35 30 20 10 5
insert : 50
 50
===============
insert : 40
 50
      40
===============
insert : 35
Not Balance, Rebalance!
      50
 40
      35
===============
insert : 30
      50
 40
      35
           30
===============
insert : 20
Not Balance, Rebalance!
      50
 40
           35
      30
           20
===============
insert : 10
Not Balance, Rebalance!
           50
      40
           35
 30
      20
           10
===============
insert : 5
Not Balance, Rebalance!
           50
      40
           35
 30
           20
      10
           5
===============

'''
# Title           : Chapter : 8 - item : 5 - ตรวจสอบว่าเป็น binary search tree หรือไม่
# Question        : จงเขียนฟังก์ชัน สำหรับตรวจสอบว่า Tree นี้เป็น binary search tree หรือไม่
#                   โดยกำหนดให้ 0<=node.data<=100 และฟังก์ชั่นมีparameterมากที่สุด4ตัว

class Node:

    def __init__(self, data) :  
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self) :
        return str(self.data) 

class Tree:
    def __init__(self) : 
        self.root = None
        self.num = 0

    def insert(self, val) :  
        if self.root == None:
            self.root = Node(val)
            self.num += 1

        else:
            h = height(self.root)
            max_node = pow(2, h + 1) - 1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num += 1
            elif self.num + 1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num += 1
            else:
                # print(max_node - ((max_node - (pow(2, h) -1)) / 2))
                if self.num + 1 <= max_node - ((max_node - (pow(2, h) -1)) / 2):
                    insert_subtree(current.left,self.num - round(pow(2, h) / 2), val)
                else:
                    insert_subtree(current.right, self.num - pow(2, h), val)
                self.num += 1


def insert_subtree(r, num, val) :
    if r != None :
        h = height(r)
        max_node = pow(2, h + 1) -1
        current = r
        if num+1 > max_node:
            while(current.left != None) :
                current = current.left
            current.left = Node(val)
            return

        elif num + 1 == max_node :
            while(current.right != None) :
                current = current.right
            current.right = Node(val)
            return

        if num + 1 <= max_node - ((max_node - (pow(2, h) -1)) / 2) :
            insert_subtree(current.left, num - round(pow(2, h) / 2), val)
        else:
            insert_subtree(current.right, num - pow(2, h), val)
    else :
        return

def height(root) :
    if root == None :
        return -1
    else :
        left = height(root.left)
        right = height(root.right)
        if left > right :
            return left + 1
        else :
            return right + 1
                       
def printTree90(node, level = 0) :
    if node != None :
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def inorder(node) :
    if node :
        _str = inorder(node.left) + str(node.data) + ' ' + inorder(node.right)
        return _str
    return ''

def preorder(node) :
    if node :
        _str = str(node.data) + ' ' + preorder(node.left) + preorder(node.right)
        return _str
    return ''

def check_binary_search_tree_(root) :
    _str = list(map(int, inorder(root).split()))
    # print(_str)
    # print(preorder(tree.root))
    if min(_str) < 0 :
         return False
    if max(_str) > 100 :
        return False

    for i in range(len(_str) - 1) :
        # print(f'\t{_str[i]} | {_str[i + 1]}')
        if _str[i] >= _str[i + 1] :
            return False
        # if not 0 <= int(_str[i]) <= 100 :
        #     return False
        # if not 0 <= int(_str[i+1]) <= 100 :
        #     return False
    return True

if __name__ == '__main__' :
    tree = Tree()
    data = input("Enter Input : ").split()
    for e in data : tree.insert(int(e))

    printTree90(tree.root)
    print(check_binary_search_tree_(tree.root))

'''
Enter Input : 2 1 3
      3
 2
      1
True


Enter Input : 1 2 3
      3
 1
      2
False


Enter Input : 1 0 5 -1
      5
 1
      0
           -1
False
'''
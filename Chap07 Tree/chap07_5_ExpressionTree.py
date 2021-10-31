# Title       ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ
# Question    ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

class Queue :
    def __init__(self) :
        self.q = []

    def enque(self, data) :
        return self.q.append(data)

    def deque(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return ''
    
    def size(self) :
        return len(self.q)
    
    def isEmpty(self) :
        return self.size() == 0

class Stack :
    def __init__(self) :
        self.s = []
    
    def push(self, data) :
        return self.s.append(data)

    def pop(self) :
        if not self.isEmpty() :
            return self.s.pop()
        return ''

    def size(self) :
        return len(self.s)

    def isEmpty(self) :
        return self.size() == 0

class Node :
    def __init__(self, data, left = None, right = None):
        self.data = data
        if left == None     : self.left = None
        else                : self.left = left
        if right == None    : self.right = None
        else                : self.right = right
        # self.left = None
        # self.right = None
    
    def __str__(self):
        return str(self.data)

class BST :
    def __init__(self) :
        self.root = None

    def insert(self, data) :
        _new = Node(data)
        
        if self.root == None :
            self.root = _new
            return
        else :
            _cur = self.root
            while _cur != None :
                if data < _cur.data :
                    if _cur.left == None :
                        _cur.left = _new
                        return self.root
                    else :
                        _cur = _cur.left

                else : # data >= _cur.data 
                    if _cur.right == None :
                        _cur.right = _new
                        return self.root
                    else :
                        _cur = _cur.right

    def printTree(self, node, level = 0) :
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preorder(self, node) : # root left right
        if node != None :
            # print(f'{node} ', end='')
            # self.preorder(node.left)
            # self.preorder(node.right)
            _str = str(node) + str(self.preorder(node.left)) + str(self.preorder(node.right))
            return _str
        return ''

    def inorder(self, node) : # left root right
        if node != None :
            # if node.right != None : print('(', end='')
            # self.inorder(node.left)
            # print(f'{node} ', end='')
            # self.inorder(node.right)
            # if node.left != None : print(')', end='')
            _str = self.inorder(node.left) + str(node) + self.inorder(node.right)
            if node.left != None and node.right != None :
                _str = '(' + _str + ')'
            return _str
        return ''            
            
    def postorder(self, node) : # left right root
        if node != None :
            # self.postorder(node.left)
            # self.postorder(node.right)
            # print(f'{node} ', end='')
            _str = self.postorder(node.left) + self.postorder(node.right) + str(node) + ' '
            return _str
        return ''             

if __name__ == '__main__' :
    T = BST()
    S = Stack()
    _input = list(input('Enter Postfix : '))
    # print(_input)
    for i in _input : 
        if i in '+-*/' :
            # Node(sign, left, right) >> [..., l , r]
            right = S.pop()
            left = S.pop()
            S.push(Node(i, left, right))
        else :
            S.push(Node(i))

    rootExp = S.pop()
    # print(f'Stack : {S}')
    # print(f'rootExp : {rootExp}')
    
    print(f'Tree :')
    T.printTree(rootExp)
    print('--------------------------------------------------')
    print(f'Infix : {T.inorder(rootExp)}')
    print(f'Prefix : {T.preorder(rootExp)}')

'''
Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de



Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg


Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg



'''
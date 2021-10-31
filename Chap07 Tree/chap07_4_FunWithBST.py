# Title       Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree
# Question    ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

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

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST :
    def __init__(self):
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

    def printTree(self, node, level = 0):
        if node != None :
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preorder(self, node) : # root left right
        if node != None :
            # print(f'{node} ', end='')
            # self.preorder(node.left)
            # self.preorder(node.right)
            _str = str(node) + ' ' + str(self.preorder(node.left)) + str(self.preorder(node.right))
            return _str
        return ''

    def inorder(self, node) : # left root right
        if node != None :
            # self.inorder(node.left)
            # print(f'{node} ', end='')
            # self.inorder(node.right)
            _str = self.inorder(node.left) + str(node) + ' ' + self.inorder(node.right)
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

    def breadth(self, node) : # root left right -> graph
        _str = ''
        if node != None :
            q = Queue()
            q.enque(node)
            while not q.isEmpty() :
                _temp = q.deque()
                _str += str(_temp) + ' '
                # print(f'{_temp} ', end='')
                
                if _temp.left != None :
                    q.enque(_temp.left)
                if _temp.right != None :
                    q.enque(_temp.right)
        return _str

    def min(self) : 
        # Left
        if not self.root == None :
            _cur = self.root
            while _cur != None :
                if _cur.left == None :
                    return _cur
                else :    
                    _cur = _cur.left
        return
                
    def max(self) :
        # Right
        if not self.root == None :
            _cur = self.root
            while _cur != None :
                if _cur.right == None :
                    return _cur
                else :    
                    _cur = _cur.right
        return

if __name__ == '__main__' :
    T = BST()
    _input = [int(i) for i in input('Enter Input : ').split()]
    for i in _input:
        root = T.insert(i)

    # print('\n==========')
    # T.printTree(root)
    # print('==========\n')

    # print(f'Preorder : ', end='')
    # T.preorder(root)
    # print(f'\nInorder : ', end='')
    # T.inorder(root)
    # print(f'\nPostorder : ', end='')
    # T.postorder(root)
    # print(f'\nBreadth : ', end='')
    # T.breadth(root)

    print(f'Preorder : {T.preorder(root)}')
    print(f'Inorder : {T.inorder(root)}')
    print(f'Postorder : {T.postorder(root)}')
    print(f'Breadth : {T.breadth(root)}')


'''
Enter Input : 10 4 20 1 5
Preorder : 10 4 1 5 20 
Inorder : 1 4 5 10 20 
Postorder : 1 5 4 20 10 
Breadth : 10 4 20 1 5 


Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 
'''
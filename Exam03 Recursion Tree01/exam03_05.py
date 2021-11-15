# Title       : Chapter : 15 - item : 5 - BST exam
# Question    : จงสร้าง BST class

# รับข้อมูล และแสดงผล

# 1. Preorder

# 2. Postorder

# 3. Inorder

# 4. Level order (Breadth)
class Queue :
    def __init__(self) :
        self.q = []

    def size(self) :
        return len(self.q)

    def isEmpty(self) :
        return self.size() == 0

    def enq(self, data) :
        return self.q.append(data)

    def deq(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return ''

class Node : 
    def __init__(self, data, left = None, right = None) :
        self.data = data
        if left == None  : self.left = None
        else             : self.left = left
        if right == None : self.right = None
        else             : self.right = right

    def __str__(self) :
        return str(self.data)

class Tree :
    def __init__(self) :
        self.root = None

    def insert(self, data) :
        if self.root == None :
            self.root = Node(data)
            return
        else :
            _node = self.root
            while _node != None :
                if data < _node.data :
                    if _node.left == None :
                        _node.left = Node(data)
                        return self.root
                    _node = _node.left
                else :
                    if _node.right == None :
                        _node.right = Node(data)
                        return self.root
                    _node = _node.right
    
    def preorder(self, node) :
        if node != None :
            _str = str(node) + ' ' + self.preorder(node.left) + self.preorder(node.right)
            return _str
        return ''

    def postorder(self, node) :
        if node != None :
            _str = self.postorder(node.left) + self.postorder(node.right) + str(node) + ' '
            return _str
        return ''

    def inorder(self, node) :
        if node != None :
            _str = self.inorder(node.left) + str(node) + ' ' + self.inorder(node.right)
            return _str
        return ''

    def breadth(self, node) :
        _str = ''
        if node != None :
            q = Queue()
            q.enq(node)
            while not q.isEmpty() :
                _cur = q.deq()
                _str += str(_cur) + ' '
                if _cur.left != None :
                    q.enq(_cur.left)
                if _cur.right != None :
                    q.enq(_cur.right)
        return _str


if __name__ == '__main__' :
    _input = list(map(int, input(' *** Binary Search Tree ***\nEnter Input : ').split()))
    # print(_input)
    t = Tree()
    for i in _input :
        root = t.insert(int(i))
    
    print('\n --- Tree traversal ---')
    print(f'Level order : {t.breadth(root)}')
    print(f'Preorder : {t.preorder(root)}')
    print(f'Inorder : {t.inorder(root)}')
    print(f'Postorder : {t.postorder(root)}')

'''
 *** Binary Search Tree ***
Enter Input : 1 2 3 4 5

 --- Tree traversal ---
Level order : 1 2 3 4 5 
Preorder : 1 2 3 4 5 
Inorder : 1 2 3 4 5 
Postorder : 5 4 3 2 1 

'''
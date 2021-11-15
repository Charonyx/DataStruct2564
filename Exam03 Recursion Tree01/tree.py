class Stack :
    def __init__(self) :
        self.s = []

    def push(self, data) :
        return self.s.append(data)

    def pop(self) :
        if not self.isEmpty() :
            return self.s.pop()
        return -1

    def size(self) :
        return len(self.s)

    def isEmpty(self) :
        return self.size() == 0

class Queue :
    def __init__(self) :
        self.q = []

    def enq(self, data) :
        return self.q.append(data)

    def deq(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return ''

    def size(self) :
        return len(self.q)

    def isEmpty(self) :
        return self.size() == 0

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

    def __str__(self) :
        return str(self.root)

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

    # def insertRecursion(self, node, data) :
    #     if node == None :
    #         return Node(data)
    #     if data < node.data :
    #         node.left = self.insertRecursion(node.left, data)
    #     else :
    #         node.right = self.insertRecursion(node.right, data)
    #     return node
        
    def delete(self, node, data) :
        if node != None :
            if data < node.data :
                node.left = self.delete(node.left, data)
            elif data > node.data :
                node.right = self.delete(node.right, data)

            elif data == node.data :
                if node.left == None :
                    # _temp = node.right
                    # node = None
                    # node = _temp
                    # return _temp
                    node = node.right
                    return node
                elif node.right == None :
                    node = node.left
                    return node
                else :
                    # MIN from right
                    _temp = node.right
                    while _temp.left != None :
                        _temp = _temp.left

                    node.data = _temp.data
                    node.right = self.delete(node.right, _temp.data)

                    # _temp = node.left
                    # while _temp.right != None :
                    #     _temp = _temp.right

                    # node.data = _temp.data
                    # node.left = self.delete(node.left, _temp.data)
        return node

    def preorder(self, node) :
        if node != None :
            _str = str(node) + ' ' + str(self.preorder(node.left)) + str(self.preorder(node.right))
            return _str
        return ''

    def inorder(self, node) :
        if node != None :
            _str = str(self.inorder(node.left)) + str(node) + ' ' + str(self.inorder(node.right))
            return _str
        return ''

    def postorder(self, node) :
        if node != None :
            _str = self.postorder(node.left) + self.postorder(node.right) + str(node) + ' '
            return _str
        return ''

    def breathfirst(self, node) :
        _str = ''
        if node != None :
            q = Queue()
            q.enq(node)
            while not q.isEmpty() :
                _temp = q.deq()
                _str += str(_temp) + ' '
                if _temp.left != None :
                    q.enq(_temp.left)
                if _temp.right != None :
                    q.enq(_temp.right)
        return _str

    def nodeMin(self) :
        if self.root != None :
            _node = self.root
            while _node != None :
                if _node.left != None :
                    _node = _node.left
                else :
                    return _node
        return ''

    def nodeMax(self) :
        if self.root != None :
            _node = self.root 
            while _node != None :
                if _node.right != None :
                    _node = _node.right
                else :
                    return _node
        return ''

    def printTree(self, node, level = 0) :
        if node != None :
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)



'''
    def printMultiTree(self, node, k, level = 0):
        if node != None:
            # print(node.data)
            if node.data > k :
                multi = 3
            else :
                multi = 1

            node.data *= multi
            if node.right :
                self.printMultiTree(node.right, k, level + 1)
            print('     ' * level, node.data)
            if node.left :
                self.printMultiTree(node.left, k, level + 1)


    def checkpos(self, data):
        if self.root is None:
            print("Not exist")
            return
        if self.root.data == data:
            print("Root")
            return

        current = self.root
        while current is not None:
            if data == current.data:
                if current.left is None and current.right is None:
                    print("Leaf")
                else:
                    print("Inner")
                return
            elif data > current.data:
                current = current.right
            else:
                current = current.left 
        print("Not exist")


    def less_than(self, node, data):
        if node == None:
            return 0

        n = self.less_than(node.left, data)
        if node.data > data:
            return n
        n += self.less_than(node.right, data)

        if node.data <= data:
            n += 1
        return n
    # print(T.less_than(root, int(k)))

def height(obj):
    if not obj:
        return -1
    a = height(obj.left) + 1
    b = height(obj.right) + 1

    return max(a, b)
'''

if __name__ == '__main__' :
    _input = list(map(int, input('Enter Input : ').split()))
    t = Tree()
    for i in _input : 
        root = t.insert(int(i))
        # t.root = t.insertRecursion(t.root, i)
    
    # print(t)
    t.printTree(root)
    print(t.nodeMin())
    print(t.nodeMax())

    print(f'preorder : {t.preorder(root)}')
    print(f'inorder  : {t.inorder(root)}')
    print(f'postorder: {t.postorder(root)}')
    print(f'breadth  : {t.breathfirst(root)}')

    print(t.delete(root, 2))
    print(f'preorder : {t.preorder(root)}')
    print(f'inorder  : {t.inorder(root)}')
    print(f'postorder: {t.postorder(root)}')
    print(f'breadth  : {t.breathfirst(root)}')

    print(t.delete(root, 22))
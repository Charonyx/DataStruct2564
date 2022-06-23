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
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self) :
        return str(self.data)

class AVL : 
    def __init__(self) :
        self.root = None

    def insert(self, node, data) :
        if not node :
            return Node(data)
        if data < node.data :
            node.left = self.insert(node.left, data)
        else :
            node.right = self.insert(node.right, data)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)

        if balance > 1 and data < node.left.data :
            print('LL re')
            return self.rightRotate(node)

        if balance < -1 and data > node.right.data :
            print('RR re')
            return self.leftRotate(node)

        if balance > 1 and data > node.left.data :
            print('LR re')
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and data < node.right.data :
            print('RL re')
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

    def getHeight(self, node) :
        if not node :
            return 0
        return node.height

    def getBalance(self, node) :
        if not node :
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def delete(self, node, data) :
        if node :
            if data < node.data :
                node.left = self.delete(node.left, data)
            elif data > node.data :
                node.right = self.delete(node.right, data)

            elif data == node.data :
                if not node.left :
                    node = node.right
                    return node
                elif not node.right :
                    node = node.left
                    return node
                else :
                    # min from right
                    _temp = node.right
                    while _temp.left :
                        _temp = _temp.left

                    node.data = _temp.data
                    node.right = self.delete(node.right, _temp.data)
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

    def printTree(self, node, level = 0) -> None :
        if node :
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

if __name__ == '__main__' :
    t = AVL() 
    root = None

    data = input("Enter Input : ").split()
    for e in data:
        print("insert :", e)
        root = t.insert(root, int(e))
        t.printTree(root)
        print("===============")

    # _input = list(map(int, input('Enter Input : ').split()))
    # t = AVL()
    # for i in _input : 
    #     print("insert :", i)
    #     t.insert(t.root, int(i))
    #     t.printTree(t.root)
    #     print("===============")
    
    # print(t)
    t.printTree(t.root)
    print(f'preorder : {t.preorder(t.root)}')
    print(f'inorder  : {t.inorder(t.root)}')
    print(f'postorder: {t.postorder(t.root)}')
    print(f'breadth  : {t.breathfirst(t.root)}')

    print(t.delete(t.root, 2))
    print(f'preorder : {t.preorder(t.root)}')
    print(f'inorder  : {t.inorder(t.root)}')
    print(f'postorder: {t.postorder(t.root)}')
    print(f'breadth  : {t.breathfirst(t.root)}')

    print(t.delete(t.root, 22))
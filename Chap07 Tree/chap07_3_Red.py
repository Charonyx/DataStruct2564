# Title       Chapter : 7 - item : 3 - สีแดงแรง 3 เท่า
# Question    ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST :
    def __init__(self):
        self.root = None
        self._red = 90

    def insert(self, data):
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
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

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
    _input = input('Enter Input : ').split('/')
    for i in _input[0].split() :
        root = T.insert(int(i))
    T.printTree(root)

    print('--------------------------------------------------')
    
    T.printMultiTree(root, int(_input[1]))


'''


'''
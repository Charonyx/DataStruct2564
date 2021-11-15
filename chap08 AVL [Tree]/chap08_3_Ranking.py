# Title       : Chapter : 8 - item : 3 - Ranking
# Question    : Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 
# และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด

class Node :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        if left == None  : self.left = None
        else             : self.left = left
        if right == None : self.right = None
        else             : self.right = right
    
    def __str__(self) :
        return str(self.data)

class AVL :
    def __init__(self) :
        self.root = None

    def insert(self, node, data) :
        if not node :
            return Node(data)
        elif data < node.data :
            node.left = self.insert(node.left, data)
        else :
            node.right = self.insert(node.right, data)
        return node
    

    def printTree(self, node, level = 0) :
        if node : # node != None :
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def rank(self, node, data) :
        if not node :
            return 0
        _rank = 0
        _rank = self.rank(node.left, data)
        if data >= node.data : 
            _rank += self.rank(node.right, data) + 1
        return _rank
    
if __name__ == '__main__' :
    _input = input('Enter Input : ').split('/')
    root = None
    t = AVL()
    for i in _input[0].split() :
        # print(i, end=' ')
        root = t.insert(root, int(i))
    # print()
    # print(root)
    t.printTree(root)
    print('--------------------------------------------------')
    print(f'Rank of {_input[1]} : {t.rank(root, int(_input[1]))}')
    

'''
Enter Input : 1 2 5 4 3 -2/4
           5
                4
                     3
      2
 1
      -2
--------------------------------------------------
Rank of 4 : 5

'''
# Title       : Chapter : 8 - item : 4 - Mondstadt
# Question    : 

class Node :
    def __init__(self, data, pos = 0) :
        self.data = data
        self.left = None
        self.right = None
        self.pos = pos

    def __str__(self) :
        return str(self.data)

class AVL :
    def __init__(self) :
        self.root = None

    def preorder(self, node) :
        if node :
            _str = str(node) + ' ' + self.preorder(node.left) + self.preorder(node.right)
            return _str
        return ''

    def insert(self, node, data, pos) :
        _new = Node(data, pos)
        if self.root == None :
            self.root = _new
            return 
        if pos == node.pos * 2 + 1 :
            node.left = _new
            return node
        if pos == node.pos * 2 + 2 :
            node.right = _new
            return node
        
        if node.left :                              # if node.left != None  :
            node.left = self.insert(node.left, data, pos)
        if node.right :                             # if node.right != None : 
            node.right = self.insert(node.right, data, pos)
        return node

    def sum(self, node) :
        if not node :
            return 0 
        _sum = 0
        if node.left :                               # if node.left != None  :
            _sum += self.sum(node.left)
        if node.right :                              # if node.left != None  :
            _sum += self.sum(node.right)
        return _sum + node.data
    
    #     if not node :
    #         return 0
    #     _sum = self.sumAll(node.left)
    #     _sum += self.sumAll(node.right) + int(node.data)
    #     return _sum
    
    def power(self, node, pos):
        if not node:
            return 0
        if pos == node.pos:
            return self.sum(node)

        _temp = self.power(node.left, pos)
        if _temp :
            return _temp
        _temp = self.power(node.right, pos)   
        return _temp
        
if __name__ == '__main__' :
    _input = input('Enter Input : ').split('/')
    t = AVL()
    _list = list(map(int, _input[0].split()))
    # print(_list)

    [t.insert(t.root, _list[i], i) for i in range(len(_list))]
    # print(t.preorder(t.root))
    # print(t.sumAll(t.root))
    print(t.sum(t.root))

    for i in _input[1].split(',') :
        i = i.split()
        x, y = t.power(t.root, int(i[0])), t.power(t.root, int(i[1]))

        if x == y   : _temp = '='
        elif x > y  : _temp = '>'
        elif x < y  : _temp = '<'
        print(f'{i[0]}{_temp}{i[1]}')

'''
Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt
ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี
โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
                พลัง    :   5  4  4  3  2  2  2
                ลำดับ  :   0  1  2  3  4  5  6
จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
    -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
    -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
    -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
            -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
            -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน


Enter Input : 5 4 4 3 2 2 2/1 2,5 6,2 0
22
1>2
5=6
2<0

Enter Input : 4 5/0 1,1 0
9
0>1
1<0
'''
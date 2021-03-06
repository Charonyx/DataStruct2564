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
Jean ????????????????????????????????????????????????????????????????????????????????????????????? Favonius ???????????? Mondstadt
???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? Mondstadt ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
??????????????????????????????????????????????????????????????????????????????????????????????????????????????? Mondstadt ?????????????????????????????????????????????????????????
                ????????????    :   5  4  4  3  2  2  2
                ???????????????  :   0  1  2  3  4  5  6
????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 7 ?????? ???????????????????????????????????????????????????????????????????????????????????? 0 ????????? 6 ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    -  ?????????????????????????????????????????? n ????????????????????????????????????????????????????????????????????????????????????????????? 2n+1 ????????? 2n+2 (?????????????????????????????????????????????????????????????????????????????????????????????????????? n ?????????????????????????????????????????????????????????????????????????????????????????????????????? n ????????????)
    -  ???????????????????????????????????????????????????????????????????????????????????? 0 - 5
    -  ?????????????????????????????????????????????????????????????????????????????? i ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ????????????
            -  ?????????????????????????????????????????? 1 ????????????????????? ?????????????????????????????????????????????????????????????????? 1 ?????????????????????????????????????????????????????????????????? ?????????????????????????????????????????? 1, 3 ????????? 4 ?????????????????????????????????????????????????????????????????????????????????????????? 1 ????????????????????? 4 + 3 + 2 = 9
            -  ?????????????????????????????????????????? 2 ????????????????????? ?????????????????????????????????????????????????????????????????? 2 ?????????????????????????????????????????????????????????????????? ?????????????????????????????????????????? 2 , 5 ????????? 6 ?????????????????????????????????????????????????????????????????????????????????????????? 2 ????????????????????? 4 + 2 + 2 = 8

????????????????????????????????????????????????????????????????????????????????????????????????????????? 1 ????????? 2 ?????????????????????????????? ???????????????????????????????????????????????????????????????????????????????????????????????? 1 ????????????????????????????????????????????????????????????????????????????????????????????????????????? 2
Jean ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? Mondstadt ?????????????????????????????? ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????


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
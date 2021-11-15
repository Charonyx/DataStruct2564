# Title       : Chapter : 8 - item : 1 - ถั่ววิเศษ
# Question    : กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้
# โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST ตามลำดับของข้อมูลนำเข้าซึ่งเป็นตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย
# โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง L หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง R
# จนกว่าจะถึงตำแหน่งที่เหมาะสมที่จะใส่ข้อมูลแล้วจึงพิมพ์ * เพื่อใส่ข้อมูลลงไปในต้นไม้

class Node :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        if left == None  : self.left = None
        else             : self.left = left
        if right == None : self.right = None
        else             : self.right = right

    def __str__(self) :
        return str(self.data)
class BST :
    def __init__(self) :
        self.root = None

    def insert(self, data) :
        _str = ''
        if self.root == None :
            _str += '*'
            self.root = Node(data)
            print(_str)
            return self.root

        _node = self.root
        while _node != None :
            if data < _node.data :
                if _node.left == None :
                    _str += 'L*'
                    _node.left = Node(data)
                    print(_str)
                    return self.root
                _str += 'L'
                _node = _node.left
            else :
                if _node.right == None :
                    _str += 'R*'
                    _node.right = Node(data)
                    print(_str)
                    return self.root
                _str += 'R'
                _node = _node.right

if __name__ == '__main__' :
    _input = input('Enter Input : ').split()
    t = BST()
    for i in _input :
        t.insert(int(i))


'''
Enter Input : 1 2 5 4 3 -2 -1
*
R*
RR*
RRL*
RRLL*
L*
LR*
'''
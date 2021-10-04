# Title       : Chapter : 5 - item : 2 - แ ต ก ดั ง เ พ ล้ ง ! ! !

class Node :
    def __init__(self, w, f, next = None) :
        self.w = w
        self.f = f
        if next == None : self.next = None
        else            : self.next = next
        
    def __str__(self) :
        return str(self.w) + '_' + str(self.f)

class LinkedList :
    def __init__(self) :
        self.head = None
        self._size = 0

    def __str__(self) :
        if not self.isEmpty() :
            _cur = self.head
            _str = 'start : ' + str(_cur.w) + '_' + str(_cur.f) + ' '
            while _cur.next != None :
                _str += str(_cur.next.w) + '_' + str(_cur.next.f) + ' '
                _cur = _cur.next
            return _str
        return ''
    
    def isEmpty(self) :
        return self.head == None

    def size(self) :
        return len(self._size)

    def enque(self, w, f) :
        self._size += 1
        _new = Node(w, f)
        if self.isEmpty() :
            self.head = _new
        else :
            _cur = self.head
            while _cur.next != None :
                _cur = _cur.next
            _cur.next = _new
    
    def deque(self) :
        if self.isEmpty() :
            return ''
        else :
            self._size -= 1
            _cur = self.head
            self.head = self.head.next
            return str(_cur.w) + '_' + str(_cur.f)

    def remove(self, w, f) :
      _cur = self.head
      while _cur.w != w or _cur.f != f :
         _cur = _cur.next
      _cur.w = _cur.next.w
      _cur.f = _cur.next.f
      _cur.next = _cur.next.next

    def rear(self) :
        if not self.isEmpty() :
            _cur = self.head
            while _cur.next != None :
                _cur = _cur.next
            return _cur.w

    def checkBroken(self) : 
        _again = True
        i = 0
        while _again :
            _cur = self.head
            while _cur.next != None :
                # print(f'Round : {i} -> {_cur}')
                if _cur.w < _cur.next.w and self.rear() > _cur.w:
                    # print(f'-----if condition-----\n\tbefore \t: {self}')
                    print(_cur.f)
                    self.remove(_cur.w, _cur.f)
                    # print(f'\tafter \t: {self}')
                    _again = True
                    break
                # print(f'-----else condition-----\n\telse \t: {self}')
                _again = False
                _cur = _cur.next
            i+=1

if __name__ == '__main__' :
    l1 = LinkedList()
    l2 = LinkedList()
    _input = input('Enter Input : ').split(',')
    for i in _input :
        i = i.split()
        l1.enque(int(i[0]), int(i[1]))
    # print(l1)
    l1.checkBroken()

        

'''
กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา  แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย  
กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร  กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก  และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน  
กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน  โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! 
และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว
ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ  ซึ่งรวมถึงขนาดของจานและความถี่ของจาน  จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด

อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

'''

'''
Enter Input : 1 10,5 20,3 30,3 40,4 50
10
40
30

Enter Input : 90 8,68 99,44 3,44 102,50 2
102
3
'''
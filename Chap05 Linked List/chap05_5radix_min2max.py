# Title       : Chapter : 5 - item : 5 - Radix Sort (น้อยไปมาก)
'''
ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบน้อยไปมาก

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )
'''
class Node :
    def __init__(self, data, next = None) : 
        self.data = data
        if next == None : self.next = None
        else            : self.next = next

    def __str__(self) :
        return str(self.data)

class LinkedList :
    def __init__(self) :
        self.head = None
        self._size = 0

    def __str__(self, mode = None) :
        if not self.isEmpty() :
            _cur = self.head
            _str = str(_cur.data) + ' '
            while _cur.next != None :
                _str += str(_cur.next.data) + ' '
                _cur = _cur.next
            if mode == 1 :
               _str = ' -> '.join(_str.split())
            return _str
        return ''

    def strShow(self) :
        return ' -> '.join((self.__str__()).split())    # CAN write this statement in the another way -> line: 28-29

    def isEmpty(self) -> None :
        return self.head == None

    def size(self)  -> int :
        return self._size

    def enqueOrigin(self, value) -> int :
        self._size += 1
        _new = Node(value)
        if self.isEmpty() :
            self.head = _new
        else :
            _cur = self.head
            while _cur.next != None :
                _cur = _cur.next
            _cur.next = _new

    def enque(self, value) -> int :
        self._size += 1
        _new = Node(value)
        if self.isEmpty() :
            self.head = _new
        else :
            _cur = self.head
            if value < _cur.data :
                _new.next = _cur
                self.head = _new
                return
            while _cur.next != None :
                if value < _cur.next.data :
                    _new.next = _cur.next
                    _cur.next = _new
                    return
                _cur = _cur.next
            _cur.next = _new


    def deque(self) -> int :
        if self.isEmpty() :
            return ''
        else :
            # print(f'-----------deque----------')
            self._size -= 1
            _cur = self.head
            self.head = self.head.next
            return _cur.data  


def getDigit(num, digit) -> int:
    # print(f'\tnum: {num}\tdigit: {digit}')
    num = abs(num)
    # if num < 0 : num *= -1
    for i in range(digit - 1) : num //= 10
    return num % 10

def getMaxBit(num)  -> int :
    i = 0
    while num > 0 : 
        num //= 10
        i += 1
    return i

def radix(l = []) :
    _input = LinkedList()
    _output = LinkedList()
    [_input.enqueOrigin(i) for i in l]
    [_output.enque(i) for i in l]
    # print(f'_input : {_input}')
    _maxBits = getMaxBit(max(l))
    # print(f'_maxbits : {_maxBits}')
    _list = list([LinkedList() for i in range(10)])
    _line = '------------------------------------------------------------\n'
    for i in range(1, _maxBits + 2) :
        print(f'{_line}Round : {i}')
        while not _output.isEmpty() :
            _temp = _output.deque()
            # print(_temp)
            # print(f'Digit : {getDigit(_temp, i)}')
            _list[getDigit(_temp, i)].enque(_temp)

        _sum = 0
        for j in range(10) :
            print(f'{j} : {_list[j]}')
            if j != 0 :
                _sum += not _list[j].isEmpty()

        if _sum == 0 :
            for j in range(10) :
                while not _list[j].isEmpty() :
                    _output.enque(_list[j].deque())
            break

        for j in range(10) :
            while not _list[j].isEmpty() :
                _output.enque(_list[j].deque())
    
    print(f'{_line}{i - 1} Time(s)')
    print(f'Before Radix Sort : {_input.__str__(1)}')
    print(f'After  Radix Sort : {_output.__str__(1)}')

    # print(f'Before Radix Sort : {_input.strShow()}')
    # print(f'After  Radix Sort : {_output.strShow()}')
        

if __name__ == '__main__' :
    _input = [int(i) for i in input('Enter Input : ').split()]
    # print(_input)
    radix(_input)
    
    


    
'''
Enter Input : 64 8 216 512 27 729 0 1 343 125
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 
2 : 512 
3 : 343 
4 : 64 
5 : 125 
6 : 216 
7 : 27 
8 : 8 
9 : 729 
------------------------------------------------------------
Round : 2
0 : 0 1 8 
1 : 216 512 
2 : 27 125 729 
3 : 
4 : 343 
5 : 
6 : 64 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 0 1 8 27 64 
1 : 125 
2 : 216 
3 : 343 
4 : 
5 : 512 
6 : 
7 : 729 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 0 1 8 27 64 125 216 343 512 729 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
After  Radix Sort : 0 -> 1 -> 8 -> 27 -> 64 -> 125 -> 216 -> 343 -> 512 -> 729




Enter Input : -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72
------------------------------------------------------------
Round : 1
0 : 0 
1 : -1 
2 : -142 2 72 
3 : -123 133 
4 : -5038594 
5 : 3645 15615 
6 : 456 
7 : 27 
8 : 668 
9 : -789 
------------------------------------------------------------
Round : 2
0 : -1 0 2 
1 : 15615 
2 : -123 27 
3 : 133 
4 : -142 3645 
5 : 456 
6 : 668 
7 : 72 
8 : -789 
9 : -5038594 
------------------------------------------------------------
Round : 3
0 : -1 0 2 27 72 
1 : -142 -123 133 
2 : 
3 : 
4 : 456 
5 : -5038594 
6 : 668 3645 15615 
7 : -789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : -789 -142 -123 -1 0 2 27 72 133 456 668 
1 : 
2 : 
3 : 3645 
4 : 
5 : 15615 
6 : 
7 : 
8 : -5038594 
9 : 
------------------------------------------------------------
Round : 5
0 : -789 -142 -123 -1 0 2 27 72 133 456 668 3645 
1 : 15615 
2 : 
3 : -5038594 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 6
0 : -5038594 -789 -142 -123 -1 0 2 27 72 133 456 668 3645 15615 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : -123 -> 456 -> -789 -> 0 -> 27 -> 3645 -> 133 -> -142 -> -5038594 -> 15615 -> 668 -> 2 -> -1 -> 72
After  Radix Sort : -5038594 -> -789 -> -142 -> -123 -> -1 -> 0 -> 2 -> 27 -> 72 -> 133 -> 456 -> 668 -> 3645 -> 15615




'''
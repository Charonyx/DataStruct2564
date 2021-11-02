
from collections import deque
from typing import Deque


class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        # s = 'Linked data : '
        s = ''
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def reverse(self) :
        if self.isEmpty() :
            return

        else :
            p = self.head
            prev = None
            while p != None :
                n = p.next
                p.next = prev
                prev = p
                p = n
            self.head = prev
        return

    def check(self, data) :
        p = self.head
        if self.isEmpty() :
            return 0
        else :
            while p.next != None :
                if p.data == data :
                    return 1
                p = p.next
            if p.data == data :
                return 1
        return 0

class Queue() :
    def __init__(self) :
        self._list = LinkedList()

    def __str__(self) :
        if not self.isEmpty() :
            result = ''
            for i in range(len(self._list)-1) :
                _data = self._list.nodeAt(i).data
                result += str(_data) + ' <- '
            return result + str(self._list.tail.data)
        return 'Empty Queue'

    def enQueue(self, data) :
        self._list.append(data)

    def deQueue(self) :
        # if not self.isEmpty() :
        return self._list.removeHead()
        # return

    def __len__(self) :
        return len(self._list)

    def isEmpty(self) :
        return len(self._list) == 0

    def checkDup(self) :

        # print('Hello')
        _check = LinkedList()
        # print('======')
        # print(_check)
        # print('======')
        # print(self)
        for i in range(len(self._list)) :
            _data = self._list.nodeAt(i).data
            # print(_data)
            # print(_check)
            # if _data not in  :
            if _check.check(_data) == 0 :
                _check.append(_data)
            else : 
                return 'Duplicate'
        return 'NO Duplicate'

    def zero(self) :
        foundZero = False
        
        if not self.isEmpty() :
            for i in range(len(self._list)) :
                _data = self._list.nodeAt(i).data
                print(f'{i} | {_data}')
                if _data == 0 :
                    print(f'\tfound {_data}')
                    break
                else :
                    self.deQueue()
                    print(f'\tlist {self._list}')
                    self.enQueue('test')
                print(f'\tlist {self._list}')

            # self.enQueue(self.deQueue())
            # print(f'list {self._list}')
        return
    '''
     *** Re order ***
    Enter Input : 2 3 1 0 4 5 6
    Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
    After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1
    '''

if __name__ == '__main__' :
    _input = input(' *** Re order ***\nEnter Input : ').split()

    q = Queue()
    for i in _input :
        q.enQueue(int(i))
    print(f"Before : {q}")
    q.zero()
    print(f"After : {q}")



'''
Chapter : 14 - item : 4 - Exam_SQL_2_4aa
 ส่งมาแล้ว 0 ครั้ง
จงเขียนโปรแกรมแบ่งการเรียงลำดับจากตัวเลขที่ป้อนเข้าไป โดยให้ส่วนต้นเริ่มที่เลข 0 ต่อด้วยส่วนท้ายของลำดับที่เหลือ ดังตัวอย่าง

การเขียนโปรแกรมนี้ให้การเขียนโปรแกรมด้วย singly linked list

ตัวอย่าง



Enter Input : 2 3 1 0 4 5 6

Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1



Enter Input : 1 0

Before : 1 <- 0

After : 0 <- 1



Enter Input : 0 1 2 3 4 5 6 7 8 9

Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9


After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9



Enter Input : 1 2 3 0

Before : 1 <- 2 <- 3 <- 0

After : 0 <- 1 <- 2 <- 3

'''




#  *** Re order ***
# Enter Input : 2 3 1 0 4 5 6
# Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
# After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1

#  *** Re order ***
# Enter Input : 1 0
# Before : 1 <- 0
# After : 0 <- 1

#  *** Re order ***
# Enter Input : 1 2 3 0
# Before : 1 <- 2 <- 3 <- 0
# After : 0 <- 1 <- 2 <- 3


#  *** Re order ***
# Enter Input : 0 1 2 3 4 5 6 7 8 9
# Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
# After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
# Chapter : 14 - item : 5 - Exam SQL_2_5aa

'''
จงเขียนโปรแกรมโดยใช้ Queue ให้สร้าง class และ method เพื่อจัดการข้อมูลโดยมีข้อมูลที่เก็บใน Queue อยู่แล้ว โดยตรวจสอบว่ามีข้อมูลซ้ำใน Queue หรือไม่ หลังจากดำเนินการแล้วเสร็จ และให้แสดงผลดังตัวอย่าง โดย

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D                -> คือการนำข้อมูลด้านหน้าออก
E <value>   -> คือการนำข้อมูล value เข้าจากด้านหลัง



ตัวอย่าง

Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D

NO Duplicate



Enter Input : 1 1 1 1/E 2,E 3,D,D


Duplicate



Enter Input : 19 22 17 6 5/E 22,D


Duplicate
'''
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
            result = 'Queue data : '
            for i in range(len(self._list)) :
                _data = self._list.nodeAt(i).data
                result += str(_data) + ' '
            return result
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

    
'''
Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate
'''

if __name__ == '__main__' :
    _input = input('Enter Input : ').split('/')

    q = Queue()
    for i in _input[0].split() :
        q.enQueue(int(i))

    # print(q)

    for i in _input[1].split(',') :
        if len(i) == 1 :
            q.deQueue()
        else :
            q.enQueue(int(i.split()[1]))
    # print(q)
    # q.checkDup()
    print(q.checkDup())
'''
    19 22 17 6 5/E 22,D

    1 2 3 4 5 6/E 7,E 8,D,D,E 7

    1 1 1 1/E 2,E 3,D,D    

    1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
'''
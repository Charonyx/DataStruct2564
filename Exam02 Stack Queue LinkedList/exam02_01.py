# Chapter : 14 - item : 1 - Exam #2 Stack Queue LinkedList 1a

'''จงสร้างโครงสร้างข้อมูล Stack ที่มี method ดังต่อไปนี้ 

__str__ สำหรบแสดงข้อมูลที่อยู่ใน stack

push(data) สำหรับเก็บข้อมูล data   

pop() สำหรับนำข้อมูลออก

isEmpty() สำหรับตรวจสอบว่า stack ว่างไหม ถ้าว่าง ให้เป็น True

size() สำหรับแสดงขนาดของ stack ว่ามีข้อมูลกี่ตัว

peek() สำหรับแสดงค่าข้อมูลที่อยู่ที่อยู่บนสุด

bottom() สำหรับแสดงค่าข้อมูลที่อยู่ล่างสุด

โดยเมื่อป้อน 1 แล้วให้ทำงานคำสั่งต่อไปนี้ '''
class Stack :
    def __init__(self, _list = None) :
        # if self._list == None : self._list = []
        # else                  : self._list = _list
            
        self._list = []

    def __str__(self) :
        result = 'Data in Stack is : '
        for i in self._list :
            result += str(i) + ' '
        return result

    def push(self, data) :
        return self._list.append(data)

    def pop(self) :
        if not self.isEmpty() :
            return self._list.pop()
        return ''

    def isEmpty(self) :
        return self.size() == 0

    def size(self) :
        return len(self._list)

    def peek(self) :
        if not self.isEmpty() :
            return self._list[-1]
        return

    def bottom(self) :
        if not self.isEmpty() :
            return self._list[0]
        return 


if __name__ == '__main__' :
    _input = int(input('Enter choice : '))

    if _input == 1 :
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())

    elif _input == 2 :
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())
    elif _input == 3 :
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())
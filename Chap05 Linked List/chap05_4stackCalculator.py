# Title       : Chapter : 5 - item : 4 - Stack Calculator
'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
'''

class Node : 
    def __init__(self, data, next = None, prev = None) :
        self.data = data
        if next == None : self.next = None
        else            : self.next = next
        if prev == None : self.prev = None
        else            : self.prex = prev

    def __str__(self) :
        return str(self.data)
        
class StackCalc :
    def __init__(self) :
        self.head = self.tail = None
        self._size = 0
        self._error = False
        
    def __str__(self) :
        if not self.isEmpty() :
            _cur = self.tail
            _str = 'start: '
            while _cur != None : 
                _str += str(_cur.data) + ' '
                _cur = _cur.prev
            return _str
        return ''
    
    def isEmpty(self) :
        return self.head == None or self.tail == None

    def push(self, data) :
        self._size += 1
        if self.isEmpty() :
            self.head = self.tail = Node(data)
        else:
            _new = Node(data)
            self.head.prev = _new
            _new.next = self.head
            _new.prev = None
            self.head = _new

    def pop(self) :
        if self.isEmpty() :
            return 0
        elif self.head.next == None :
            self._size -= 1
            _temp = self.head.data
            self.head = None
            return _temp
        else :
            self._size -= 1
            _temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return _temp

    def peek(self) :
        if not self.isEmpty() :
            return self.head.data
        elif not self._error :
            return 0
        return ''

    def size(self):
        return self._size
        # _temp = self.head
        # _count = 0
        # while _temp is not None:
        #     _count = _count + 1
        #     _temp = _temp.next
        # return _count

    def run(self, instructions) :
        # print(instructions)
        for i in instructions :
            if i == 'POP' :
                self.pop()
            elif i == 'DUP' :
                self.push(self.peek())
            else :
                try : 
                    # print(int(i))
                    self.push(int(i))
                except : 
                     if i   == '+' : self.push(self.pop() + self.pop())
                     elif i == '-' : self.push(self.pop() - self.pop())
                     elif i == '*' : self.push(self.pop() * self.pop())
                     elif i == '/' : self.push(self.pop() // self.pop())
                     else : 
                         print(f'Invalid instruction: {i}')
                         self._error = True
                         break
        # print(self)
    
if __name__ == '__main__' : 
    print("* Stack Calculator *")
    arg = input("Enter arguments : ").split()
    machine = StackCalc()
    machine.run(arg)
    print(machine.peek())



'''
* Stack Calculator *
Enter arguments : 5 6 +
11

* Stack Calculator *
Enter arguments : 3 DUP +
6

* Stack Calculator *
Enter arguments : 6 5 5 7 * - /
5

* Stack Calculator *
Enter arguments : a b c +
Invalid instruction: a

* Stack Calculator *
Enter arguments : 12
12

* Stack Calculator *
Enter arguments : 9 14 DUP + - 3 POP
19

* Stack Calculator *
Enter arguments : 1 2 3 4 5 POP POP POP
2

* Stack Calculator *
Enter arguments : 13 DUP 4 POP 5 DUP + DUP + -
7

* Stack Calculator *
Enter arguments : 4 POP
0

'''
# Title       : Chapter : 5 - item : 3 - MergeOrderList
'''
จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

****ห้ามสร้าง Class LinkList****
'''
class node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None : self.next = None
        else            : self.next = next

    def __str__(self):
        return str(self.data)

def createList(l = []) :
    # print(l)
    l = list(map(int, l.split(',')))
    # [print(i, end=' ') for i in l]
    # print(f'\n list = {l}')
    _new = node(l[0])
    _head = _new
    for i in l[1:] :
        _new.next = node(i)
        # _head.next = _new
        _new = _new.next      
    return _head

def printList(H) :
    _str = ''
    while H != None :
        # print(H)
        _str += str(H) + ' '
        H = H.next
    print(_str)

def mergeOrderesList(p, q) :
    m = None
    if p.data < q.data :
        m = node(p)
        p = p.next
    else : 
        m = node(q)
        q = q.next
    _head = m

    while p != None and q != None :
        if p.data < q.data :
            m.next = p
            p = p.next
        else : 
            m.next = q
            q = q.next
        m = m.next

    while p != None :
        m.next = p
        p = p.next
        m = m.next
    while q != None :
        m.next = q
        q = q.next
        m = m.next
    return _head

if __name__ == '__main__' :
    L1, L2 = list(input('Enter 2 Lists : ').split())
    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ',end='')
    printList(LL1)
    print('LL2 : ',end='')
    printList(LL2)
    m = mergeOrderesList(LL1,LL2)
    print('Merge Result : ',end='')
    printList(m)


'''
Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 

Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
LL1 : 1 4 5 5 6 7 
LL2 : 2 3 6 9 10 
Merge Result : 1 2 3 4 5 5 6 6 7 9 10 

Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
LL1 : 2 2 2 10 
LL2 : 1 1 1 1 5 5 5 6 7 8 
Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10 

'''
# Title       : Chapter : 5 - item : 1 - รู้จักกับ Singly Linked List

class Node:
    def __init__(self, data, next = None) :
        self.data = data                          # data
        if next == None : self.next = None
        else            : self.next = next        # link

class LinkedList:
    def __init__(self, head = None) :
        if head == None :
            self.head = self.tail = None
            self._size = 0
        else : 
            self.head = head
            cur = self.head
            self._size = 1
            while cur.next != None :
                cur = cur.next
                self._size += 1
            self.tail = cur

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        self._size += 1
        node = Node(data)               # creat Node
        if not self.isEmpty() :         # self.head != None
            cur = self.head
            while cur.next != None :    # node.next != None
                cur = cur.next
            cur.next = node
        else :
            self.head = node
            # self.tail = node

    def addHead(self, item):
        self._size += 1
        node = Node(item)               # new node
        if not self.isEmpty() :
            cur = self.head
            self.head = node
            self.head.next = cur        # shift head
        else :
            self.head = node
            # return

    def search(self, data):
        cur = self.head
        if not self.isEmpty() :
            while cur.next != None :
                if cur.data == data :
                    # print(f'{cur.data} == {data}')
                    return 'Found'
                cur = cur.next
            if cur.data == data :
                return 'Found'
        return 'Not Found'             

    def index(self, data):
        index = 0
        cur = self.head

        if not self.isEmpty() :
            if self.size() == 1 :
                if cur.data == data :
                    return index
            while cur.next != None :
                if cur.data == data :
                    # print(f'{cur.data} == {data}')
                    return index
                cur = cur.next
                index += 1
            if cur.data == data :
                return index
        return -1

    def size(self):
        return self._size
        # cur = self.head
        # total = 0
        # while cur.next != 0 :
        #     total += 1
        #     cur = cur.next
        # return total

    def pop(self, pos):
        index = 0
        cur = self.head
        if pos < 0 or pos >= self.size() :
            return 'Out of Range'
        if pos == 0 and self.size() == 1 :
            self.head = self.tail = None
        elif pos == 0 :
            cur.next = None
            cur = cur.next
        else :                          
            while index != pos - 1 :
                index += 1
            # 1 pop(2) 3 -> 1 3 | cur.next = cur.next.next 
            cur.next = (cur.next).next
            # cur2 = cur.next
            # cur  = cur2.next
        self._size -= 1
        return 'Success'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
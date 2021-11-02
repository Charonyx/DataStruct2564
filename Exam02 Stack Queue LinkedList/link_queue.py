# singly linked list


class Node :
    def __init__(self, data, next = None) :
        self.data = data
        if self.next == None : self.next = None
        else                 : self.next = next
        
    def __str__(self) :
        return str(self.data)

class linkedlist :
    def __init__(self, head = None) :
        if head == None : 
            self.head = self.tail = None
            self._size = 0
        else :
            self.head = head
            _cur = self.head
            while _cur.next != None :
                _cur = _cur.next
                self._size += 1
            _cur = self.tail

    def __str__(self) :
        result = ''
        _cur = self.head
        while _cur != None :
            result += str(_cur.data) + ' '
            _cur = _cur.next
        return result

    def __len__(self) :
        return self.size()

    def size(self) :
        # self._size = 0
        # if not self.isEmpty() :
        #     _cur = self.head
        #     while _cur.next != None :
        #         self._size += 1
        #         _cur = _cur.next
        return self._size

    def isEmpty(self) :
        return self.size() == 0

    def append(self, data) :
        _cur = self.head
        self._size += 1
        if self.head == None :
            self.head = self.tail = Node(data, None)
        else :
            self.tail.next = Node(data, None)           # link to next node
            self.tail = Node(data, None)                # shift to next node

    def removeHead(self) :                              # 3 case
        if self.isEmpty() :                             # 1. None
            return
        elif self.size() == 1 :                         # 2. size == 1 || self.head.next == None
        # elif self.head.next == None :
            _cur = self.head
            self.head = self.tail = None 
            self._size -= 1
        else :                                          # 3. size > 1
            _cur = self.head
            self.head = self.head.next
            self._size -= 1
        return _cur.data

    def nodeAt(self, i) :
        _cur = self.head
        for j in range(i) :
            _cur = _cur.next
        return _cur

class Queue :
    def __inti__(self, _list) :
        self._list = linkedlist()

    def __str__(self) :
        # return str(self._list)
        if not self.isEmpty() :
            result = ''
            for i in range(len(self._list)) :
                _data = self._list.nodeAt(i).data
                result += str(_data) + ' '
            return result
        return 'Empty'

    def __len__(self) :
        return len(self._list)

    def enQueue(self, data) :
        return self._list.append(data)

    def deQueue(self) :
        if not self.isEmpty() :
            return self._list.removeHead()
        return 'Empty'

    def isEmpty(self) :
        return len(self._list) == 0


if __name__ == '__main__':
    # print(123)
    # test = linkedlist()
    # test.size()

    # test.append(123)
    # print(test.size())
    # print(str(test.head))

    choice = int(input('Enter choice : '))
    if choice == 1:
        q1 = Queue()
        q1.enQueue(10)
        q1.enQueue(20)
        q1.enQueue(30)
        print(q1)
        q1.deQueue()
        q1.enQueue(40)
        print("Size of Queue :", len(q1))
        print(q1)
    elif choice == 2:
        q1 = Queue()
        q1.enQueue(100)
        q1.enQueue(200)
        q1.enQueue(300)
        q1.deQueue()
        print(q1)
        print("Queue is Empty :", q1.isEmpty())
    elif choice == 3:
        q1 = Queue()
        q1.enQueue(11)
        q1.enQueue(22)
        q1.enQueue(33)
        q1.deQueue()
        q1.deQueue()
        q1.deQueue()
        print(q1)
        print("Size of Queue :", len(q1))
        print("Queue is Empty :", q1.isEmpty())               
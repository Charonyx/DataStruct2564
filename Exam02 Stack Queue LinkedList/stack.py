class Stack :
    def __init__(self, _list = None) :
        if _list == None : self._list = []
        else             : self._list = _list

    def __str__(self) :
        result = ''
        for i in self._list : result += str(i) + ' '
        return result

    def push(self, data) :
        return self._list.append(data)
    
    def pop(self) :
        if not self.isEmpty() :
            return self._list.pop()
        return -1

    def isEmpty(self) :
        return self.size() == 0
    
    def size(self) :
        return len(self._list)

    def peek(self) :
        if not self.isEmpty() :
            return self._list[-1]
        return -1

    def bottom(self) :
        if not self.isEmpty() :
            return self._list[0]
        return -1


if __name__ == '__main__':
    s1 = Stack()
    choice = int(input("Enter choice : "))
    if choice == 1:
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())
    elif choice == 2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())
    elif choice == 3:
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())
    
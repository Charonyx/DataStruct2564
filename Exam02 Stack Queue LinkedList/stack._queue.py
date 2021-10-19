# Stack
class Stack :
    def __init__(self, _list = None) :
        if _list == None : self._list = []
        # else             : self._list = _list
        else             : [self.push(i) for i in _list]

    def __str__(self) :
        return self._list

    def push(self, value) :
        return self._list.append(value)

    def pop(self) :
        if not self.isEmpty() :
            return self._list.pop()
        return 'Empty'

    def peek(self) :
        if not self.isEmpty() :
            return self._list[-1]
        return 'Empty'
    
    def size(self) :
        return len(self._list)

    def isEmpty(self) :
        return self.size() == 0

# Queue
class Queue :
    def __init__(self, _list = None) :
        if _list == None : self._list = []
        # else             : self._list = _list
        else             : [self.enq(i) for i in _list]
        
    def __str__(self) :
        return self._list
    
    def enq(self, value) :
        return self._list.append(value)

    def deq(self) :
        if not self.isEmpty() :
            return self._list.pop(0)
        return 'Empty'

    def size(self) :
        return len(self._list)

    def isEmpty(self) :
        return self.size() == 0

    def rear(self) :
        if not self.isEmpty() :
            return self._list[0]
        return 'Empty'

    def  tail(self) :
        if not self.isEmpty() :
            return self._list[-1]
        return 'Empty'


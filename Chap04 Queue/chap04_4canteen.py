# Title       : Chapter : 4 - item : 4 - Canteen

class Queue :
    def __init__(self, q = None) :
        if q == None : self.q = []
        else         : self.q = q
    def enque(self, value):
        for i in self.q[-1::-1] : #range(self.size() -1, -1 , -1)
            if value[0] == i[0] :
                if self.q.index(i) == self.size() - 1 : break
                # print(self.q.index(i), i)
                self.q.insert(self.q.index(i) + 1, value)
                return
        self.q.append(value)
        # print(f'\tenque -> {value} \t{self.q}')
    def deque(self) :
        if not self.isEmpty() :
            return self.q.pop(0)[1]
        return 'Empty'
    def front(self) :
        return self.q[0]
    def rear(self) :
        return self.q[-1]
    def isEmpty(self) :
        return self.size() == 0
    def size(self) : 
        return len(self.q)
        
if __name__ == '__main__' :
    inputq  = input('Enter Input : ').split('/')

    q       = Queue()
    human   = {}
    for i in inputq[0].split(',') : 
        # print(f'value: {i}')
        i = i.split()
        human[i[1]] = human.get(i[1], i[0])
        # print(f'human {i[1]} {i[0]}')
    # print(human)
    for i in inputq[1].split(',') :
        data = i.split()
        if data[0] == 'D' :
            print(q.deque())
            # deq = q.deque()
            # print(f'\tdeq -> {deq}')
        else :
            data[0] = human[data[1]]
            # print(f'start enque {data}')
            q.enque(data)
    # print(q.q)
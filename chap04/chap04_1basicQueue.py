# Title       : Chapter : 4 - item : 1 - Basic Queue

class Queue :
    def __init__(self, q = None) :
        if q == None : self.q = []
        else         : self.q = q
    def enque(self, value) :
        return self.q.append(value)
    def deque(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return 'Empty'
    def size(self) :
        return len(self.q)
    def isEmpty(self) :
        return self.size() == 0

if __name__ == '__main__' :
    x = input('Enter Input : ')
    q = Queue()

    for i in x.split(',') :
        if len(i) > 1 :
            q.enque(i[2::])
            print(f'Add {i[2::]} index is {q.size() - 1}')
        elif i[0] == 'D' and q.size() > 0 :
            print(f'Pop {q.deque()} size in queue is {q.size()}')
        else :
            print(-1)
    if q.size() > 0 :
        print(f'Number in Queue is :  {q.q}') 
    else :
        print('Empty')
'''
from collections import deque


x = input('Enter Input : ').split(',')
q = deque()

for i in range(len(x)) :
    if x[i][0] == 'E' :
        q.append(x[i][2::])
        print(f'Add {x[i][2::]} index is {len(q) - 1}')
    elif x[i][0] == 'D' and len(q) > 0 :
        print(f'Pop {q.popleft()} size in queue is {len(q)}')
    else :
        print(-1)
if len(q) > 0 :
    print(f'Number in Queue is :  {(q.__str__())[6:-1]}') 
else :
    print('Empty')
'''
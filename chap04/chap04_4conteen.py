# Title       : Chapter : 4 - item : 4 - Canteen

class Queue :
    def __init__(self, q = None) :
        if q == None : self.q = []
        else         : self.q = q
    def enque(self, value) :
        return self.q.append(value)
    def deque(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return print('Empty')
    def front(self) :
        return self.q[0]
    def rear(self) :
        return self.q[-1]
    def isEmpty(self) :
        return self.size() == 0
    def size(self) : 
        return len(self.q)
        
if __name__ == '__main__' :
    que, cmd = input('Enter Input : ').split('/')
    que, cmd = que.split(','), cmd.split(',')
    allq = [i for i in que]
    # print(allq)
    allq = [Queue() for i in range(len(que))]

    for i in range(len(cmd)) :
        # print(cmd[i], end=' ')
        if len(cmd[i]) == 1 : continue
        else                : allq[0].enque(int(cmd[i][2::]))
    # print('\n cmd que -> ', end='')
    # print(allq[0].q)
    for i in range(len(que)) :
        # print(int(que[i][0]), end=' ')
        allq[int(que[i][0])].enque(int(que[i][2::]))

    showq, showq2 = Queue(), Queue()
    for i in range(len(allq)) :
        if i == 0 or allq[i].isEmpty() : continue
        for j in allq[i].q :
            if j in allq[0].q : 
                showq.enque(j)
    # print(f'showq = {showq.q}')
    j = 0
    for i in range(len(cmd)) : 
        if len(cmd[i]) == 1 : 
            showq2.deque()
        else : 
            showq2.enque(showq.q[j])
            print(showq.q[j])
            j += 1
        # print(showq2.q)


'''
Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
Empty
101
201

Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D
Empty
101
102
201
Empty

'''
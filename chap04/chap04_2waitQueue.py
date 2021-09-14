# Title           : Chapter : 4 - item : 2 - แถวคอย

class Queue :
    def __init__(self) :
        self.q = []
    def enqueue(self, value) :
        self.q.append(value)
    def dequeue(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return -1
    def isEmpty(self) :
        return self.size() == 0
    def size(self) :
        return len(self.q)
    def getQueue(self) :
        return self.q

if __name__ == '__main__' :
    p, t = input('Enter people and time : ').split()
    t = int(t)
    q1, q2, q3 = Queue(), Queue(), Queue()
    for i in p : q1.enqueue(i)
    # print(q1.getQueue())
    t1 = t2 = 0
    for i in range(1, t + 1) :
        if t1 % 3 == 0 and not q2.isEmpty():
            q2.dequeue()
            t1 = 0
        if t2 % 2 == 0 and not q3.isEmpty() :
            q3.dequeue()
            t2 = 0

        if q2.size() < 5 and not q1.isEmpty()   : q2.enqueue(q1.dequeue())
        elif q3.size() < 5 and not q1.isEmpty() : q3.enqueue(q1.dequeue())
        if not q2.isEmpty() : t1 += 1
        if not q3.isEmpty() : t2 += 1
        
        print(f'{i} {q1.getQueue()} {q2.getQueue()} {q3.getQueue()}')
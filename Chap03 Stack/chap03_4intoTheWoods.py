# Title       : Chapter : 3 - item : 4 - Into the Woods

class Stack:
    def __init__(self) :
        self.s = []
    def push(self, value) :
        return self.s.append(value)
    def pop(self) :
        if not self.isEmpty() :
            return self.s.pop()
        return 0
    def peek(self) :
        if not self.isEmpty() :
            return self.s[-1]
        return 0
    def isEmpty(self) :
        return self.size() == 0
    def size(self) : 
        return len(self.s)
    def getStack(self) :
        return self.s
    def getStackIndex(self, index) :
        return self.s[index]
        

if __name__ == '__main__' :
    x = input('Enter Input : ').split(',')
    s = Stack()
    for i in range(len(x)) :
        if x[i][0] == 'A' :
            s.push(int(x[i][2::]))
        elif x[i][0] == 'B' :
            count = 0
            hight = -1
            for j in range(s.size() -1, -1, -1) :
                if s.getStackIndex(j) > hight :
                    hight = s.getStackIndex(j)
                    count += 1
                # print(s.getStackIndex(j))
            print(count)
            
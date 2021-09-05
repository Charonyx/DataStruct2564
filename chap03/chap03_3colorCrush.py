# Title       : Chapter : 3 - item : 3 - Color_Crush
class Stack:
    def __init__(self) :
        self.color = []
    def push(self, value) :
        return self.color.append(value)
    def pop(self) :
        if not self.isEmpty() :
            return self.color.pop()
        return -1
    def peek(self) :
        if not self.isEmpty() :
            return self.color[-1]
        return -1
    def size(self) :
        return len(self.color)
    def isEmpty(self) :
        return self.size == 0
    def getStack(self) :
        return self.color
    def getStackIndex(self, index) :
        return self.color[index]
    def __str__(self) :
        return [print(i, end='') for i in self.color]

# def crush() :
    

color = input('Enter Input : ').split()
stack = Stack()
[stack.push(i) for i in color]


while 1 :
    combo = 0
    crush = False
    nowColor = stack.peek()
    stack2 = Stack()
    for i in range(stack.size() -1, -1, -1) : # range(stack.size() -1, -1, -1)
        # if color[i] == color[i - 1] == color[i - 2] :
        if stack.getStackIndex(i) == stack.getStackIndex(i - 1) and stack.getStackIndex(i - 1) == stack.getStackIndex(i - 2) and i >= 2 :
            combo += 1
            # pop 
        else :
            stack2.push(stack.getStackIndex(i))
        stack.pop()
    print(stack.getStack())
    print(stack2.getStack())

    for i in range(stack2.size() -1, -1, -1) :
        stack.push(stack2.getStackIndex(i))
        stack2.pop()
    print(stack.getStack())
    print(stack2.getStack())

    break
        # if len(color) >= 3 and color[i] = color[i-1]
            
#         S.push(i)



print(stack.getStack())
print(stack2.getStack())

print(stack.size())
stack.__str__()

'''
Enter Input : G H H H H P
3
PHG


Enter Input : L C C X X X C D
2
DL
Combo : 2 ! ! !

Enter Input : C C C
0
Empty

Enter Input : A
1
A

Enter Input : A B B A
4
ABBA
'''
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
        return [print(self.getStackIndex(i), end='') for i in range(self.size() -1, -1, -1)]

if __name__ == '__main__' :
    color = input('Enter Input : ').split()
    stack = Stack()
    [stack.push(i) for i in color]
    combo = 0
    loopAgain = True
    stack2 = Stack()
    while loopAgain :
        nowColor = stack.peek()
        j = int()
        for i in range(stack.size() -1, 0, -1) :
            if i == j - 1 or i == j - 2 : 
                stack.pop()
                continue
            if stack.getStackIndex(i) == stack.getStackIndex(i - 1) == stack.getStackIndex(i - 2) and (not stack.getStackIndex(i) == stack.getStackIndex(-1) or not i == 1) :
                combo += 1
                j = i
                if stack.size() == 3 : stack.pop()  
            else : stack2.push(stack.getStackIndex(i))
            stack.pop()
        for i in range(stack2.size() -1, -1, -1) :
            stack.push(stack2.getStackIndex(i))
            stack2.pop()
        for i in range(stack.size() -1, 0, -1) :
            if stack.getStackIndex(i) == stack.getStackIndex(i - 1) == stack.getStackIndex(i - 2) :
                loopAgain = True
                break
            else : loopAgain = False
        if stack.size() <= 1 : break
    # print(stack.getStack())
    # print(stack2.getStack())
    print(stack.size())
    if stack.getStack() == []   : print('Empty')
    else                        : 
        stack.__str__()
        print()
    if combo >= 2               : print(f'Combo : {combo} ! ! !')

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
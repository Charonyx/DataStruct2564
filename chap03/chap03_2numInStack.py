# Title           : Chapter : 3 - item : 2 - Number in Stack

class Stack :
    def __init__(self) :
        self.num = []
    def push(self, value) :
        return self.num.append(value)
    def pop(self) :
        if not self.isEmpty() :
            return self.num.pop()
        return -1
    def peek(self) :
        if not self.isEmpty() :
            return self.num[-1]
        return -1
    def isEmpty(self) :
        return self.size() == 0
    def size(self) : 
        return len(self.num)
    def getStack(self) :
        return self.num
    def getStackIndex(self, index) :
        return self.num[index]
    def __str__(self) :
        return f'Value in Stack = {self.getStack()}'

def manageStack(x) :
    stack = Stack()
    for i in range(len(x)) :
        if x[i][0] == 'A' :
            stack.push(int(x[i][2::]))
            print(f'Add = {x[i][2::]}')

        elif x[i][0] == 'P' : 
            if not stack.isEmpty()  : print(f'Pop = {stack.pop()}')
            else                    : print(-1)

        elif ((x[i][0] == 'D' and int(x[i][2::]) in stack.getStack()) or x[i][0] == 'L' or x[i][0] == 'M') and not stack.isEmpty() :
            # print('condition LD MD : ', end='')
            stack2 = Stack()
            # count = 0 # USE count if you want to delete only one element in stack
            for j in range(stack.size() -1, -1, -1) :  
                if x[i][0] == 'D' :
                    if not int(x[i][2::]) == stack.getStackIndex(j) : #or count > 0:
                        stack2.push(stack.getStackIndex(j))
                        
                    elif int(x[i][2::]) == stack.getStackIndex(j) : #and count == 0 :
                        print(f'Delete = {x[i][2::]}')
                        # count += 1
                    else : print(-1)
                    stack.pop()

                elif x[i][0] == 'L' :
                    # print(f'not {int(x[i][3::])} > {stack.getStackIndex(j)}')
                    if not int(x[i][3::]) > stack.getStackIndex(j) :
                        stack2.push(stack.getStackIndex(j))
                    elif int(x[i][3::]) >= stack.getStackIndex(j):
                        print(f'Delete = {stack.getStackIndex(j)} Because {stack.getStackIndex(j)} is less than {x[i][3::]}')
                    else : print(-1)
                    stack.pop()

                elif x[i][0] == 'M' :
                    # print(f'not {int(x[i][3::])} < {stack.getStackIndex(j)}')
                    if not int(x[i][3::]) < stack.getStackIndex(j) :
                        stack2.push(stack.getStackIndex(j))
                    elif int(x[i][3::]) <= stack.getStackIndex(j) :
                        print(f'Delete = {stack.getStackIndex(j)} Because {stack.getStackIndex(j)} is more than {x[i][3::]}')
                    else : print(-1)
                    stack.pop()

            for j in range(stack2.size() -1, -1, -1) :
                stack.push(stack2.getStackIndex(j))
        elif stack.isEmpty() : print(-1)
        
    print(stack.__str__())
    
if __name__ == '__main__' :
    x = input('Enter Input : ').split(',')
    manageStack(x)
# Title           : Chapter : 3 - item : 1 - รู้จักกับ STACK

from collections import deque

stack = deque()
x = input('Enter Input : ').split(',')

for i in range(len(x)) :
    if x[i][0] == 'A' :
        stack.append(int(x[i][2::]))
        print(f'Add = {x[i][2::]} and Size = {len(stack)}')
    elif x[i][0] == 'P' : 
        if len(stack) > 0 : 
            print(f'Pop = {stack[-1]} and Index = {len(stack) - 1}')
            stack.pop()
        else :
            print(-1)

# print(stack)
print(f'Value in Stack = ', end='')
if len(stack) > 0 :
    [print(i, end=' ') for i in stack]
else :
    print('Empty')
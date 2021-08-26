print('*** Fun with Drawing ***')
num = int(input('Enter input : '))
k   = 2 * num - 2
for i in range(-k, k + 1) :
    for j in range(-k, k + 1) :
        if (i > j and i + j > 0) or (i < j and i + j < 0) : 
            if i % 2 == 0       : print('#', end='')
            else                : print('.', end='')
        elif (i < j and i + j > 0) or (i > j and i + j < 0) : 
            if j % 2 == 0       : print('#', end='')
            else                : print('.', end='') # left right
        else : 
            if (i + j) % 2 == 0 and (i % 2 == 0 or j % 2 == 0) : print('#', end='')    
            else                :print('.', end='')
    print('')
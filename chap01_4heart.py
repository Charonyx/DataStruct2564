print('*** Fun with Drawing ***')
num = int(input('Enter input : '))

if num >= 2 :
    k = 4 * num - 3
    l = 3 * num - 2
    for i in range(l):
        for j in range(-(k // 2), (k // 2) + 1):
            if 0 <= i < num :
                if num - i == abs(j) + 1 or num - -i == abs(j) + 1  : print('*', end='')
                elif num - i <= abs(j) < num + i                    : print('+', end='')
                else                                                : print('.', end='')
            else : 
                if l - i == abs(j) + 1                              : print('*', end='')
                elif l - i > abs(j) + 1                             : print('+', end='')
                else                                                : print('.', end='')
        print()
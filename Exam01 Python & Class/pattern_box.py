_input = int(input('Enter Input : '))
if 0 < _input < 16 :
    _input = _input + 1
    for i in range(1, _input) :
        # if i < 10 : temp
        # print(i)           
        for j in range(1, _input) :
            if i == 1 :
                print((hex(j).upper())[2:], end=' ')                        #! [2:] to substring 0x
            elif i == _input - 1 :
                print((hex(_input - j ).upper())[2:], end=' ')              #! [2:] to substring 0x
            elif j == 1 :
                print((hex(i).upper())[2:], end=' ')
            elif j == _input - 1 :
                print((hex(i - 1).upper())[2:], end=' ')
            else :
                print('', end='  ')
        print()
else : print('Enter between  1 - 15')
    
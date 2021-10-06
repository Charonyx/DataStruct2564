# Chapter : 12 - item : 2 - exam_python_1_2564_2a

def check(n) :
    _list = []
    for i in range(1, n+1) :
        if n % i == 0 :
            # print(i)
            _list.append(i)
    print(f'Output ==> ', end='')
    print(*_list)
    print(f'Total ==> {len(_list)}')

print(' *** Divisible number ***')
_input = int(input('Enter a positive number : '))

if _input > 0 :
    check(_input)
else :
    print(f'{_input} is OUT of range !!!')

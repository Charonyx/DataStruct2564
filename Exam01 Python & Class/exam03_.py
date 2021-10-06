# Chapter : 12 - item : 3 - exam_python_1_2564_3a

print(' *** String count ***')
_input = input('Enter message : ')

_countUp = {}
_countLow = {}
for i in _input :
    if 'a' <= i <= 'z' :
        if i not in _countLow.keys() :
            # print('eiei')
            _countLow[i] = 1
        else :
            _countLow[i] += 1
    if 'A' <= i <= 'Z' :
        if i not in _countUp.keys() :
            _countUp[i] = 1
        else :
            _countUp[i] += 1

print(f'No. of Upper case characters : {sum(_countUp.values())}')
print(f'Unique Upper case characters : ', end='')
# print(*sorted(_countUp.keys()))
# print(_countUp.keys())
for i in sorted(_countUp.keys()) : print(i, end='  ')
print(f'\nNo. of Lower case Characters : {sum(_countLow.values())}')
print(f'Unique Lower case characters : ', end='')
# print(*sorted(_countLow.keys()))
for i in sorted(_countLow.keys()) : print(i, end='  ')
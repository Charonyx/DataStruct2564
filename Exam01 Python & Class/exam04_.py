# Chapter : 12 - item : 4 - exam_python_1_2564_4a

print('*** String Rotation ***')
_input = input('Enter 2 strings : ').split()
i = 0
l1 = _input[0]
l2 = _input[1]
# print(l1)
# print(l2)
pline = True
while 1:
    _input[1] = _input[1][1:] + _input[1][0:1]
    _input[0] = _input[0][-1:] + _input[0][0:-1]
    i += 1
    if i <= 5 :
        print(f'{i} {_input[0]} {_input[1]}')
    elif pline and i != 6:
        print(' . . . . . ')
        pline = False
    if _input[0] == l1 and _input[1] == l2 :
        break
if not pline or i == 6 :
    print(f'{i} {_input[0]} {_input[1]}')
print(f'Total of  {i} rounds.')
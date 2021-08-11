print('*** Rabbit & Turtle ***')
d, vr, vt, vf = map(int, input('Enter Input : ').split())
print('{:.2f}'.format(vf * abs(d / (vr - vt))))
# print('%.2f' % (vf * abs(d / (vr - vt))))
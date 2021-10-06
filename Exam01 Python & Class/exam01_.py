# Chapter : 12 - item : 1 - exam_python_1_2564_1a

print(' *** Wind classification ***')
_input = float(input('Enter wind speed (km/h) : '))
if _input < 0 :
    print('!!!Wrong value can\'t classify.')
elif 0 <= _input < 52 :
    print('Wind classification is Breeze.')
elif _input < 56 :
    print('Wind classification is Depression.')
elif _input < 102 :
    print('Wind classification is Tropical Storm.')
elif _input < 209 :
    print('Wind classification is Typhoon.')
else :
    print('Wind classification is Super Typhoon.')


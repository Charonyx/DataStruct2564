# Title           : Chapter : 2 - item : 3 - Odd And Even

def odd_evenL(data, choice) :
    dataList2 = []
    for i in data :
        # index start with 0 but position start with 1
        if choice == 'Even' and data.index(i) % 2 != 0 : 
            dataList2.append(i)

        elif choice == 'Odd' and data.index(i) % 2 == 0 :
            dataList2.append(i)
        
    print(dataList2)

def odd_evenS(data, choice) :
    for i in data :
        if choice == 'Even' and data.index(i) % 2 != 0 :
            print(i, end='')

        elif choice == 'Odd' and data.index(i) % 2 == 0 :
            print(i, end='')


print('*** Odd Even ***')
dataType, data, choice = input('Enter Input : ').split(',')
if dataType == 'S' : 
    odd_evenS(data, choice)

elif dataType == 'L' :
    dataList = data.split()
    odd_evenL(dataList, choice)
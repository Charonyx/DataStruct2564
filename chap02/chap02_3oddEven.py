# Title           : Chapter : 2 - item : 3 - Odd And Even
# Question        : ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

# def odd_even(arr, s):
#     //Code Here

# โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List
# Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา
# Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่

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

'''
# ----------------------- TESTCASE ZONE -----------------------
# TESTCASE 1
*** Odd Even ***
Enter Input : S,ABCDEF,Odd
ACE

# TESTCASE 2
*** Odd Even ***
Enter Input : L,1 2 3 4 5,Even
['2', '4']

# TESTCASE 3
*** Odd Even ***
Enter Input : S,ABC12345DEF,Even
B135E

# TESTCASE 4
*** Odd Even ***
Enter Input : S,ABC12345DEF,Odd
AC24DF

# TESTCASE 5
*** Odd Even ***
Enter Input : L,ABC12345DEF,Even
[]

# TESTCASE 6
*** Odd Even ***
Enter Input : L,ABC12345DEF,Odd
['ABC12345DEF']

# TESTCASE 7
*** Odd Even ***
Enter Input : L,A B C 1 2 3 4 5 D E F,Odd
['A', 'C', '2', '4', 'D', 'F']

# TESTCASE 8
*** Odd Even ***
Enter Input : L,A B C 1 2 3 4 5 D E F,Even
['B', '1', '3', '5', 'E']

'''
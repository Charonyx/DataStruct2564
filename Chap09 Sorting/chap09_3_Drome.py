# Title       : Chapter : 9 - item : 3 - somethingDROME
# Question    : รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้
#             - น้อยไปมาก และไม่มีตัวซ้ำ  "Metadrome"
#             - น้อยไปมาก และมีตัวซ้ำ    "Plaindrome"
#             - มากไปน้อย และไม่มีตัวซ้ำ  "Katadrome"
#             - มากไปน้อย และมีตัวซ้ำ    "Nialpdrome"
#             - ทุกหลักเป็นเลขเดียวกันหมด "Repdrome"
#             - ไม่อยู่ในเงื่อนไขด้านบนเลย  "Nondrome"
#             ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def checkASC(list) :
    for i in range(len(list) - 1) :
        if list[i] > list[i + 1] :
            return False
    return True

def checkDES(list) :
    for i in range(len(list) - 1) :
        if list[i] < list[i + 1] :
            return False
    return True

def checkDup(list) :
    if not set([i for i in list if list.count(i) > 1]) :
        return False
    return True
    
def checkAllDup(list) :
    for i in range(len(list) - 1) :
        if list[i] != list[i + 1] : 
            return False
    return True

def checkDrome(list) :
    isASC = checkASC(list)
    isDES = checkDES(list)
    isDUP = checkDup(list)

    if checkAllDup(list) : 
        return 'Repdrome'
    elif isASC :
        if isDUP : return 'Plaindrome'
        else     : return 'Metadrome'
    elif isDES :
        if isDUP : return 'Nialpdrome'
        else     : return 'Katadrome'
    else :
        return 'Nondrome'

if __name__ == '__main__' :
    _input = input('Enter Input : ')
    _list = []
    [_list.append(int(i)) for i in _input]
    # print(_list)
    # print(checkDup(_list))
    print(checkDrome(_list))


'''
Enter Input : 1357
Metadrome

Enter Input : 12344
Plaindrome

Enter Input : 7531
Katadrome
'''
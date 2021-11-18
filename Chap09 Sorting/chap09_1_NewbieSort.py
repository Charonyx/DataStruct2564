# Title       : Chapter : 9 - item : 1 - หัดใช้ Sort
# Question    : ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No
#               ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง


def  isSort(list) :
    for i in range(len(list) - 1) :
        if list[i] >= list[i+1] :
            return 'No'
    return 'Yes'

if __name__ == '__main__' :
    _input = list(map(int, input('Enter Input : ').split()))
    print(isSort(_input))


'''
Enter Input : -99 -1 0 1 2 3
Yes

Enter Input : 5252 -5 2630 -558
No

Enter Input : 9 10 99
Yes

'''
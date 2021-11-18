# Title       : Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ
# Question    : ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
#               ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

# Selection
def sortDontCare(list) :
    for last in range(len(list) -1, -1, -1) :
        if list[last] < 0 :
            continue
        max = list[0]
        maxIndex = 0
        for i in range(1, last + 1) :
           if list[i] > max :               # Ascending
               max = list[i]
               maxIndex = i
        # Swap max and last
        list[last], list[maxIndex] = list[maxIndex], list[last]
    print(*list)

if __name__ == '__main__' :
    _input = list(map(int, input('Enter Input : ').split()))
    sortDontCare(_input)

'''
Enter Input : 6 3 -2 5 -8 2 -2
2 3 -2 5 -8 6 -2

Enter Input : 6 5 4 -1 3 0 2 -99 1
0 1 2 -1 3 4 5 -99 6
'''
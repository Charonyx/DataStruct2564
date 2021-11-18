# Title       : Chapter : 9 - item : 5 - Sort Subset
# Question    : ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /
# 1. ด้านซ้าย เป็นผลลัพธ์
# 2. ด้านขวา เป็น list ของจำนวนเต็ม
# โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้
# 1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
# 2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก
# ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset
# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

def selectionSort(list) :
    for last in range(len(list) -1, -1, -1) :
        max = list[0]
        maxIndex = 0
        for i in range(1, last + 1) :
            # Ascending
            if list[i] > max :
                max = list[i]
                maxIndex = i
        # Swap max and last
        list[last], list[maxIndex] = list[maxIndex], list[last]    
    return list

def sortLen(list) :
    for i in range(len(list) -1) :
        swap = False
        for j in range(len(list) - i - 1) :
            if len(list[j]) > len(list[j + 1]) :
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True
        if not swap:
            break
    # print(*list, sep='\n')
    return print('No Subset') if list == [] else print(*list, sep='\n')

# Knapsack problem
def subset(l, s, i = 0, out = [], temp = []):  
    if i >= len(l) :
        return out
    temp.append(l[i])
    if sum(temp) == s:
        out.append(temp.copy())
    out = subset(l, s, i + 1, out, temp)
    temp.pop()
    out = subset(l, s, i + 1, out, temp)
    return out
    
if __name__ == '__main__' :
    _input = input('Enter Input : ').split('/')
    _list = list(map(int, _input[1].split()))
    # print(_input[0])
    # print(_list)

    sortLen(subset(selectionSort(_list), int(_input[0])))


'''
Enter Input : 2/-2 3 1 -1 0 -3 2
[2]
[-1, 3]
[0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]

Enter Input : 2/1 0 2 -1
[2]
[0, 2]
[-1, 1, 2]
[-1, 0, 1, 2]

Enter Input : 3/-1 0 1 2
[1, 2]
[0, 1, 2]

Enter Input : 5/1 2 3 4
[1, 4]
[2, 3]

Enter Input : 4/-1 0 1 2
No Subset
'''
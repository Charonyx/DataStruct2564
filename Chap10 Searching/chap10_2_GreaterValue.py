# Title       : Chapter : 10 - item : 2 - First Greater Value
# Question    : ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

def bi_search(l, r, arr, x):
    # [l] ---- [m] ---- [r]
    if l > r : 
        if l == len(arr) :
            return 'No First Greater Value'
        return arr[l]

    m = (l + r) // 2
    # print(f'm={m} | {x} : {arr[m]}')

    if x < arr[m]   : return bi_search(l, m - 1, arr, x)
    elif x > arr[m] : return bi_search(m + 1, r, arr, x)
    elif arr[-1] != arr[m] : return arr[m + 1]

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in k :
    print(bi_search(0, len(arr) - 1, sorted(arr), i))

'''
Enter Input : 3 2 7 6 8/5
6

Enter Input : 3 2 7 6 8/5 6 12
6
7
No First Greater Value

# ***** อธิบาย Test Case 2:
# Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
# 1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
# 2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
# 3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
'''
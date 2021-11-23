# Title       : Chapter : 10 - item : 1 - หัดใช้ Binary Search
# Question    : ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

# ***** อธิบาย Input
# 1. ด้านซ้าย  จะเป็น list ของ Data
# 2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    # [l] ---- [m] ---- [r]
    if l > r : 
        return False

    m = (l + r) // 2
    # print(f'm={m} | {x} : {arr[m]}')

    if x < arr[m]   : return bi_search(l, m - 1, arr, x)
    elif x > arr[m] : return bi_search(m + 1, r, arr, x)
    else            : return True

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

'''
Enter Input : 33 2 11 82 77 28 15 76 9 64/28
True

Enter Input : 33 2 11 82 77 28 15 76 9 64/50
False
'''
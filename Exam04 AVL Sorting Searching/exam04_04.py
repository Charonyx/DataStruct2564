# Title : Chapter : 16 - item : 4 - shell sort 1
# จงเขียนโปรแกรม shell sort ให้ได้ผลลัพธ์ตามตัวอย่าง โดยใช้ increment sequence เป็น 3 และ 1
count = 0
def shellSort(array, n):
    global count
    # print(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                count += 1
            array[j] = temp
        interval //= 2
    return array

# def shellSort(arr:list, size:int):
#     global count
#     interval = size // 2
#     while interval > 0:
#         for index_i in range(interval, size):
#             temp = arr[index_i]
#             index_j = index_i
#             while index_j >= interval and arr[index_j - interval] > temp:
#                 arr[index_j] = arr[index_j - interval]
#                 index_j -= interval
#                 count += 1
#             arr[index_j] = temp
#             count += 1
#         interval //= 2
                
#     return arr


if __name__ == '__main__' :
    print(' *** Shell sort ***')
    _input = list(map(int, input('Enter some numbers : ').split()))
    # print(_input)
    a = shellSort(_input, len(_input))
    # print(f'\nSorted -> ', end='')
    print(a)
    print(f'Data comparison =  {count}')

'''
 *** Shell sort ***
Enter some numbers : 1 2 3 4 5 6 7 8 9 10

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Data comparison =  16

'''
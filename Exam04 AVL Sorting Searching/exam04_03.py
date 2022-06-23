# Title : Chapter : 16 - item : 3 - bubble sort 1

# จากตัวอย่างการแสดงผลต่อไปนี้

#  *** ฺBubble sort ***
# Enter some numbers : 4 69 98 52 30 12 54 19 16 27

# [4, 12, 16, 19, 27, 30, 52, 54, 69, 98]
# Data comparison = 42

# ให้นักศึกษาเติมฟังก์ชั่น bubble_sort(A) ให้สมบูรณ์ 

def bubble_sort(a):
    global count 
    count = 0
    swap = True
    x = -1
    while swap:
        swap = False
        x += 1
        for i in range(1, len(a)-x):
            count += 1
            if a[i-1] > a[i] :
                a[i-1], a[i] = a[i], a[i-1]
                swap = True
    return a

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)

'''
 *** Bubble sort ***
Enter some numbers : 10 9 8 7 6 5 4 3 2 1

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Data comparison = 45
'''
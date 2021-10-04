# Title           : Chapter : 6 - item : 5 - วาดภาพแสนสุข
def staircase(n):
    if n == 0   : return 'Not Draw!'
    elif n > 0  : stairPos(n, 1)
    else        : stairNeg(abs(n), 0)
    return ''

def stairPos(n, k) :
    # print(n,k)
    print('_' * (n - k) + '#' * k)
    if k + 1 <= n   :  stairPos(n, k + 1)
    if k == n       : return
    return   

def stairNeg(n, k) :
    print('_' * k + '#' * (n - k))
    if k + 1 < n    : stairNeg(n, k + 1)
    if k == n       : return
    return 
    
if __name__ == '__main__' :
    print(staircase(int(input("Enter Input : "))))


'''
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว


Enter Input : 3
__#
_##
###

Enter Input : 7
______#
_____##
____###
___####
__#####
_######
#######

Enter Input : -8
########
_#######
__######
___#####
____####
_____###
______##
_______#


Enter Input : 2
_#
##

Enter Input : 0
Not Draw!


'''
# Title           : Chapter : 15 - item : 3 - Exam_3_3_1a
# Question        : จงเขียนโปรแกรมแบบ Recrusive สำหรับหา หรม. ของเลข 2 ตัว แล้วให้แสดงผลดังตัวอย่าง

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว

# บทนิยาม

# ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว

def gcd(a, b) :
    if a == 0 or b == 0 :
        return abs(b) if a == 0 else abs(a)
    return gcd(b, a % b)

if __name__ == '__main__' :
    a, b = input('Enter Input : ').split()
    a = int(a)
    b = int(b)
    # print(a)
    # print(b)
    if a == 0 and b == 0 :
        print(f'Error! must be not all zero.')
    elif a < 0 and b < 0 :
        print(f'The gcd of {min(a, b)} and {max(a, b)} is : {gcd(a, b)}')
    else :
        print(f'The gcd of {max(a, b)} and {min(a, b)} is : {gcd(a, b)}')

'''
Enter Input : 100 0
The gcd of 100 and 0 is : 100

Enter Input : -26 -82
The gcd of -82 and -26 is : 2

Enter Input : 100 -98
The gcd of 100 and -98 is : 2

Enter Input : 0 -80
The gcd of 0 and -80 is : 80
'''
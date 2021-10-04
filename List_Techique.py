if __name__ == '__main__' :
    num = list(map(int, input('Enter your List : ').split(',')))
    print(num)
    print(num[2:])      # ตัด 2 ตัวแรก
    print(num[2::])     # ตัด 2 ตัวแรก
    print(num[-1:])     # เอาแค่ตัวสุดท้าย
    print(num[:-1])     # ยกเว้นตัวสุดท้าย
    print(num[-1::-1])  # reverse
    print(num[::-1])    # reverse
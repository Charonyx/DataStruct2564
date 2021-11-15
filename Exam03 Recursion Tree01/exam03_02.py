# Title       : Chapter : 15 - item : 2 - Exam_3_2_1a
# qUESTION    : จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่า Max ของข้อมูลที่ป้อนเข้ามา แล้วแสดงผลดังตัวอย่าง

def max(_list) :
    if len(_list) == 1 :
        return _list[0]
    else :
        _list2 = max(_list[1:])
        # if _list2 > _list[0] :
        #     return _list2
        # else :
        #     return _list[0]
    return _list2 if _list2 > _list[0] else _list[0]

if __name__ == '__main__' :
    _input = list(map(int, input('Enter Input : ').split()))
    # print(_input)
    print(f'Max : {max(_input)}')

'''
Enter Input : 541 212 22 0 -9562262 323 5 2 9
Max : 541
'''
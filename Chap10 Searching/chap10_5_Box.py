# Title       : Chapter : 10 - item : 5 - กล่องสินค้า
# Question    : มีสินค้าอยู่ n ชิ้น โดยชิ้นที่ i (0 <= i < n) มีน้ำหนัก Wi กิโลกรัม  นำสินค้าบรรจุใส่กล่องไม่เกิน k ใบ โดยมีเงื่อนไขว่า
#               1. สิ่งของต้องมีน้ำหนักรวมกันไม่เกินน้ำหนักมากสุดที่กล่องรับไหว
#               2. หากสิ่งของชิ้นที่ a และชิ้นที่ b อยู่ในกล่องเดียวกัน (a <= b) สิ่งของทุกชิ้นที่อยู่ระหว่างสองชิ้นนี้ 
#                  (ทุกชิ้นที่ i ที่ a < i < b) จะต้องอยู่ในกล่องนี้ด้วย หาว่าใช้กล่องที่รับน้ำหนักได้น้อยสุดเท่าใดและใช้กล่องครบทุกใบ

def box(s, w) :
    index = s
    while w - _input[0][index] >= 0 :
        w -= _input[0][index]
        index += 1
        if index >= len(_input[0]) :
            break
    return index

def isValid(weight, l, b) :
    index = 0

    for i in range(b) :
        index = box(index, weight)
        if index >= len(l) :
            return True

    if index >= len(_input[0]) :
        return False

if __name__ == '__main__' :
    _input = input('Enter Input : ').split('/')
    _input[0] = list(map(int, _input[0].split()))
    _input[1] = int(_input[1])
    w = max(max(_input[0]), sum(_input[0])//_input[1])

    while True:
        if isValid(w, _input[0], _input[1]) :
            break
        w += 1

    print(f'Minimum weigth for {_input[1]} box(es) = {w}')


# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง สินค้า n ชิ้น และแต่ละชิ้นมีน้ำหนัก W กิโลกรัม
#     -   ด้านขวาหมายถึง จำนวนกล่อง k ใบ
# คำใบ้  Optimization Problem

# อธิบาย Test Case #1
# มีสินค้าอยู่ 5 ชิ้น โดยมีน้ำหนักเป็น 6 2 4 3 7 ตามลำดับ และมีกล่องจำนวน 3 ใบ   
# และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 8 กิโลกรัม 
# กล่องที่ 1 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 6 และ 2 
# กล่องใบที่ 2 จะใส่สินค้า 2 ชิ้นที่มำน้ำหนัก 4 และ 3
# กล่องใบที่ 3 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 7

'''
Enter Input : 6 2 4 3 7/3
Minimum weigth for 3 box(es) = 8

Enter Input : 8 7 2 5 1 10 9 2 3 5/5
Minimum weigth for 5 box(es) = 14

Enter Input : 19 1 2 3 4/1
Minimum weigth for 1 box(es) = 29

Enter Input : 19 1 2 3 4/2
Minimum weigth for 2 box(es) = 19

Enter Input : 6 4 9 3 1 8 5 2/5
Minimum weigth for 5 box(es) = 10
'''
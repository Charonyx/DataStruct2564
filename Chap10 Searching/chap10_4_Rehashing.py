# Title       : Chapter : 10 - item : 4 - Rehashing
# Question    : ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
#               1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
#               2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

# หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11
# การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

class Hash:
    def __init__(self, size, max, threshold) :
        self.item = list([None] * size)
        self.size = size
        self.max = max
        self.threshold = threshold
        self.nonspace = 0
        print('Initial Table :\n' + self.__str__())

    def __str__(self) :
        _str = ''
        for i in range(self.size):
            _str += f'#{i+1}\t{self.item[i]}\n'
        return _str + '----------------------------------------'

    def nearDoublePrime(self) :
        for i in range(self.size * 2, self.size + 40) :
            for j in range(2, i) :
                if i % j == 0 :
                    break
                if i - 1 == j :
                    return i

    def rehash(self, list) : 
        self.item = [None] * self.nearDoublePrime()
        self.nonspace = 0
        self.size = len(self.item)
        for i in list :
            if i != None :
                self.insert(i)

    def insert(self,data) :
        index = int(data) % self.size
        while True:
            for i in range(1,self.max + 1) :
                if  int(((self.nonspace + 1) / self.size) * 100 ) > self.threshold :
                    print('****** Data over threshold - Rehash !!! ******')
                    return True
                if self.item[index] == None :
                    self.item[index] = str(data)
                    self.nonspace += 1
                    return
                else :
                    print(f'collision number {i} at {index}')
                    if i >= self.max :
                        print('****** Max collision - Rehash !!! ******')
                        return True
                    index =data % self.size + i ** 2
                    index %= self.size

if __name__ == '__main__' :
    print(' ***** Rehashing *****')
    _input = input('Enter Input : ').split('/')

    size, max, threshold = [int(e) for e in _input[0].split()]
    h = Hash(size, max, threshold)

    store = []
    for i in _input[1].split():
        store.append(int(i))
        print(f'Add : {int(i)}')
        
        if h.insert(int(i)):
            h.rehash(store)
        print(h)


# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

'''
 ***** Rehashing *****
Enter Input : 5 1 67/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
#1	None
#2	1
#3	None
#4	None
#5	None
----------------------------------------
Add : 6
collision number 1 at 1
****** Max collision - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
----------------------------------------
'''
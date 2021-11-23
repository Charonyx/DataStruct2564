# Title       : Chapter : 10 - item : 3 - Fun with hashing
# Question    : ให้น้องเขียน Hashing โดยมีการทำงานดังนี้
#               1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
#               2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
#               3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
#               4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! (แสดงเพียง 1 ครั้ง)

class Data:
    def __init__(self, key, value) :
        self.key = key
        self.value = value

    def __str__(self) :
        return '({0}, {1})'.format(self.key, self.value)

class hash:
    def __init__(self, size, max) :
        self.item = [None] * size
        self.size = size
        self.max = max

    def __str__(self) :
        _str = ''
        for i in range(self.size):
            _str += f'#{i+1}	{self.item[i]}\n'
        return _str + '---------------------------'
        
    def isFull(self) :
        if None in self.item :
            return False
        return True

    def insert(self, data) :
        sum = 0
        for i in data.key :
            sum += ord(i)
        
        if self.isFull() :
            print('This table is full !!!!!!')
            return True

        index = sum % self.size 
        for i in range(1,self.max + 1) :
            
            if self.item[index] == None :
                self.item[index] = str(data)
                return
            else :
                print(f'collision number {i} at {index}')
                index = sum % self.size + i ** 2
                index %= self.size
        print('Max of collisionChain')


if __name__ == '__main__' : 
    print(' ***** Fun with hashing *****')
    _input = input('Enter Input : ').split('/')

    size, max = _input[0].split()
    h = hash(int(size), int(max))

    for i in _input[1].split(',') :
        key,value = i.split()
        if h.insert(Data(key, value)) :
            break
        print(h)


# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

'''
 ***** Fun with hashing *****
Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
#1	(1+1, I)
#2	None
#3	None
---------------------------
collision number 1 at 0
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
collision number 1 at 0
collision number 2 at 1
Max of collisionChain
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
#1	(1+1, I)
#2	(OnE, Love)
#3	(#$ew2, KMITL)
---------------------------
This table is full !!!!!!
'''
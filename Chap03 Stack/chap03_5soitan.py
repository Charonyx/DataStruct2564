# Title       : Chapter : 3 - item : 5 - ซอยตัน

class Stack:
    def __init__(self, max) :
        self.max = max
        self.cars = []
    def push(self, value) :
        if not value == 0 :
            return self.cars.append(value)
    def pop(self) :
        if not self.isEmpty() :
            return self.cars.pop()
        return -1
    def peek(self) :
        if not self.isEmpty() :
            return self.cars[-1]
        return -1
    def size(self) :
        return len(self.cars)
    def sizeMax(self) :
        return self.max
    def isEmpty(self) :
        return self.size() == 0
    def getStack(self) :
        return self.cars
    def getStackIndex(self, index) :
        return self.cars[index]
    
if __name__ == '__main__' :
    print("******** Parking Lot ********")
    m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
    m, n = int(m),int(n)

    stack = Stack(m)
    for i in list(map(int, s.split(','))) :
        stack.push(int(i))
    # print(stack.getStack())

    if o == 'arrive' :
        if stack.size() == stack.sizeMax() : 
            print(f'car {n} cannot arrive : Soi Full')
        elif not n in stack.getStack(): 
            stack.push(n)
            print(f'car {n} arrive! : Add Car {n}')
        elif n in stack.getStack() :
            print(f'car {n} already in soi')

    elif o == 'depart' :
        if stack.isEmpty() :
            print(f'car {n} cannot depart : Soi Empty')
        elif not n in stack.getStack() :
            print(f'car {n} cannot depart : Dont Have Car {n}')
        elif n in stack.getStack() :
            stack2 = Stack(m)
            for i in range(stack.size() -1, -1, -1) :
                if not stack.getStackIndex(i) == n : 
                    stack2.push(stack.getStackIndex(i))
                stack.pop()
            for i in range(stack2.size() -1, -1, -1) : 
                stack.push(stack2.getStackIndex(i))
            print(f'car {n} depart ! : Car {n} was remove')

    print(stack.getStack())    

    

'''
******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
car 5 arrive! : Add Car 5
[1, 2, 3, 4, 5]

******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
car 5 cannot arrive : Soi Full
[1, 2, 3, 4]

******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 1
car 1 already in soi
[1, 2, 3, 4]

******** Parking Lot ********
Enter max of car,car in soi,operation : 8 1,4,6,2,3,5,8 arrive 7
car 7 arrive! : Add Car 7
[1, 4, 6, 2, 3, 5, 8, 7]


******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 depart 3
car 3 cannot depart : Soi Empty
[]

******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,3,2 depart 1
car 1 depart ! : Car 1 was remove
[3, 2]


******** Parking Lot ********
Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
car 1 cannot depart : Dont Have Car 1
[2, 3, 5, 7, 8]

******** Parking Lot ********
Enter max of car,car in soi,operation : 5 7,3,2,1,4 depart 7
car 7 depart ! : Car 7 was remove
[3, 2, 1, 4]


'''
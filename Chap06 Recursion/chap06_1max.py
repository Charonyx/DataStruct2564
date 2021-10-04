# Title           : Chapter : 6 - item : 1 - หาค่ามากที่สุด

def findMax(numlist) :
    # print(numlist)
    if len(numlist) == 1 :
        return numlist[0]
    else :
        numMax = findMax(numlist[1:])
        return numMax if numlist[0] < numMax else numlist[0]
    
if __name__ == '__main__' :
    num = list(map(int, input('Enter Input : ').split()))
    # print(num)
    # print(len(num))
    print(f'Max : {findMax(num)}')
    
    
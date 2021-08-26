# Title       : Chapter : 2 - item : 4 - 3 SUM(2)

def sumEq5(n) :
    m = []
    for i in range(len(n)) :
        # print(n[i], end=' ')
        for j in range(i + 1, len(n)) :
            # print(n[j], end=' ')
            for k in range(j + 1, len(n)) :
                # print(n[k], end=' ')
                if n[i] + n[j] + n[k] == 5 and (([n[i], n[j], n[k]] not in m) and ([n[i], n[k], n[j]] not in m) and ([n[j], n[i], n[k]] not in m) and ([n[j], n[k], n[i]] not in m) and ([n[k], n[i], n[j]] not in m) and ([n[k], n[j], n[i]] not in m)) :
                    m.append([n[i], n[j], n[k]])
    return m    

    # sort ได้ 2 แบบ : 
    # 1. sort แล้วค่อยส่ง 
    # 2. ส่งแล้ว เอาคำตอบมา sort -> แต่อันนี้จะต้องวนลูป เพราะ เป็น list ใน list

    # for i in m : i.sort()
    # return m.sort()
    
dataList = []
num = input('Enter Your List : ').split()

if len(num) > 2 :
    for i in num : dataList.append(int(i))
    dataList.sort()
    print(sumEq5(dataList))
    # print(dataList)
else :
    print('Array Input Length Must More Than 2')
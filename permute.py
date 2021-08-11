import math
from collections import OrderedDict
print("*** Fun with permute***")
permuteList = [[]]
myList = [int(e) for e in input("input : ").split(",")]

print("Original Cofllection: "+str(myList))
print("Collection of distinct numbers:")
myList.reverse()
permuteList.append(myList)
c = 0

for i in range(len(set(myList))):
    for j in range(len(set(myList))-1):
        temp = []
        count = 0
        if(j == len(set(myList)) or j+1 >=len(set(myList)) ):
            myList[0],myList[-1] = myList[-1],myList[0]
            
        else:
            myList[j],myList[j+1] = myList[j+1],myList[j]
        temp = myList.copy()
        for k in permuteList:
            if temp == k:
                print(temp, end=" ")
                # print("k: "+str(k))
                count+=1
        if(count<1):
            permuteList.append()
            print(permuteList)
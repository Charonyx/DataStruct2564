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


# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n-r, -1))
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i+1:] + indices[i:i+1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return

# REF : https://stackoverflow.com/questions/23318787/how-do-i-create-a-permutation-on-python-without-using-the-itertools-module-nor-r
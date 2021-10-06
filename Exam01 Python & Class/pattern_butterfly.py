n = int(input('Enter Input : '))
n = n-1
# for i in range(-k, k + 1) :
#     for j in range(-n, n + 1) :
#         # print(abs(i), end='')
#         if j != 0 :
#             if abs(j) + abs(i) <= 2*abs(n) -2:
#                 print('_', end='')
#             else : 
#                 print(abs(j) + abs(i) , end='')
        

#         # if i == 0 :
#         #     print('*', end='')
#         # if j == 0 :
#         #     pass
#         # else :
#         #     print('.', end='')

#     print()


# n = 5
for i in range(-n, n + 1):
    for j in range(1, (n + 1) - abs(i) + 1):
       print("*",end="")
    for j in range(1, 2 * abs(i) + 1):
       print(" ", end="")
    for j in range(1, (n + 1) - abs(i) + 1):
       print("*", end="")
    print("")
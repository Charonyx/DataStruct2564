print('*** Election ***')
num     = int(input('Enter a number of voter(s) : '))
voter  = []
if num >= 0 and num <= 20:  
    # for i in range(num):
    #     x = int(input())
    #     voter.append(x)
    voter = list(map(int,input().split()))
    # print(max(set(voter), key = voter.count)) if 1 <= max(set(voter), key = voter.count) <= 20 else print("*** No Candidate Wins ***")
    # for i not in range()

    if 1 <= max(set(voter), key = voter.count) <= 20 :

        print(max(set(voter), key = voter.count))
    else : 
        print("*** No Candidate Wins ***")

def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

# print(most_common(voter))
print('=======')
print(voter)
print(voter.__str__())
print(max(list(voter), key = voter.index))
print(list(voter), key = voter.count)

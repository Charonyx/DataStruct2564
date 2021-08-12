print('*** Election ***')
num             = int(input('Enter a number of voter(s) : '))
voter           = []
voter2          = []
if num > 0:
    voter       = list(map(int,input().split()))
    for i in voter: 
        if 1 <= i <= 20 : voter2.append(i)
    voter.clear()
    voter = voter2.copy()
    
    # print(len(voter2))

    if voter2 == [] : print("*** No Candidate Wins ***")
    else :
        if len(voter2) == 1:
            print(max(set(voter2), key = voter2.count))
        elif len(voter2) > 1:
            voter2.remove(max(set(voter2), key = voter2.count))
            if voter.count(max(set(voter), key = voter.count)) == voter2.count(max(set(voter2), key = voter2.count)) : 
                print("*** No Candidate Wins ***")
            else : 
                print(max(set(voter), key = voter.count))

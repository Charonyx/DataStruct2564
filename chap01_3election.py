# Title       : Chapter : 1 - item : 3 - Election
# Question    : โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

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

'''
# ----------------------- TESTCASE ZONE -----------------------
# TESTCASE 1
*** Election ***
Enter a number of voter(s) : 10
6 8 13 9 8 1 16 19 4 20
8 

# TESTCASE 2
*** Election ***
Enter a number of voter(s) : 2
-1 -2
*** No Candidate Wins ***

'''
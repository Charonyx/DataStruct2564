# Title           : Chapter : 2 - item : 5 - ต่อคำหรรษา
# Question        : ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

# 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# จะไม่สามารถพูดว่า “Apple” ได้อีก

# 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที

# 3. Ignore Case Sensitive

# โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# - P < word > จะเป็นการต่อคำ
# - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# - X เป็นการระบุว่าจบการทำงาน

# โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุด
class Torkham :
    def __init__(self, word) : 
        self.word = word
        self.torkhamList = []
        self.wordGame()

    def wordAppend(self, w) :
        if self.torkhamList == [] or (str(w).lower())[:2] == (''.join(map(str, self.torkhamList))).lower()[-2:] : 
            self.torkhamList.append(w)
            print(f'\'{w}\' -> {self.torkhamList}')
        else :
            print(f'\'{w}\' -> game over')

    def wordRestart(self) :
        self.torkhamList.clear()
        print('game restarted')

    def wordExit(self) :
        exit()

    def wordGame(self) :
        for i in range(len(self.word)) :
            word[i]
            if word[i] == 'P'      : 
                # print(f'\t\t {i} : {word[i + 1]}')
                self.wordAppend(word[i + 1]) 
            elif word[i] == 'R'    : self.wordRestart()
            elif word[i] == 'X'    : self.wordExit()
            elif word[i - 1] == 'P' : continue
            else : 
                print(f'\'{word[i]} {word[i + 1]}\' is Invalid Input !!!')
                break

if __name__ == '__main__' :
    print('*** TorKham HanSaa ***')
    word    = input('Enter Input : ').split(',')
    word2   = [] 
    for i in word : word2.append(i.split())
    word.clear()
    for i in word2 :
        for j in i : word.append(j)
    Torkham(word)
    
'''
# ----------------------- TESTCASE ZONE -----------------------
# TESTCASE 1
*** TorKham HanSaa ***
Enter Input : P Apple,P LEMON,R,P onion,X
'Apple' -> ['Apple']
'LEMON' -> ['Apple', 'LEMON']
game restarted
'onion' -> ['onion']

# TESTCASE 2
*** TorKham HanSaa ***
Enter Input : P apple,p lemon,P onion,X
'apple' -> ['apple']
'p lemon' is Invalid Input !!!

# TESTCASE 3
*** TorKham HanSaa ***
Enter Input : P apPLE,P leMON,R,P Durian,P ant,P pineapple,X
'apPLE' -> ['apPLE']
'leMON' -> ['apPLE', 'leMON']
game restarted
'Durian' -> ['Durian']
'ant' -> ['Durian', 'ant']
'pineapple' -> game over

# TESTCASE 4
*** TorKham HanSaa ***
Enter Input : R,R,P KK,R,P apple,R,P Lemon,R,X
game restarted
game restarted
'KK' -> ['KK']
game restarted
'apple' -> ['apple']
game restarted
'Lemon' -> ['Lemon']
game restarted

# TESTCASE 5
*** TorKham HanSaa ***
Enter Input : P apple,P lemon,P nectarine,X
'apple' -> ['apple']
'lemon' -> ['apple', 'lemon']
'nectarine' -> game over

'''
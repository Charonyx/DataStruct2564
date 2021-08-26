# Title           : Chapter : 2 - item : 5 - ต่อคำหรรษา

class Torkham :
    torkhamList = []
    def __init__(self, word) : 
        self.word = word
        print('torkham')
        print(self.word)
        self.wordGame()

    def wordSubstring(self) :
        return self.word.split()

    def wordAppend(self) :
        # print(self.word[-2 : -1])
        # print(self.torkhamList[-1][-2:-1])
        if 1 : # self.word[-2 : -1] == self.torkhamList[-1][-2:-1] : 
            self.torkhamList.append()
        else :
            print('game over')

    def wordRestart(self) :
        self.torkhamList.clear()
        print('game restarted')

    def wordExit(self) :
        print('end')

    def wordGame(self) :
        for i in self.word :
            if len(self.word) > 1 :
                for j in range(len(i)) :
                    if j[0] == 'P' : self.wordAppend(j[1]) 
                    elif j[0] == 'R' : self.wordRestart()
                    elif j[0] == 'X' : self.wordExit()
                    else : pass
            else :
                if j == 'P' : self.wordAppend(j[1]) 
                elif j == 'R' : self.wordRestart()
                elif j == 'X' : self.wordExit()
                else : pass

if __name__ == '__main__' :
    print('*** TorKham HanSaa ***')
    txt = input('Enter Input : ').split(',')
    print(txt)
    word = [] 
    for i in txt :
        word.append(i.split())
    # print(word)
    # Torkham(txt)

    
    
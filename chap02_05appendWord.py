# Title           : Chapter : 2 - item : 5 - ต่อคำหรรษา

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
    
# Title       : 

class Stack :
    def __init__(self, s = None) :
        if s == None : self.s = []
        else         : self.s = s
    def push(self, value) :
        return self.s.append(value)
    def insert(self, index, value) :
        self.s.insert(index, value)
    def pop(self, index = None) :
        if not self.isEmpty() :
            if index == None :
                return self.s.pop()
            return self.s.pop(index)
        return -1
    def size(self) :
        return len(self.s)
    def isEmpty(self) :
        return self.size == 0
    def __str__(self, re) : #reverse == 1
        if re == 0 :
            return ''.join(i for i in self.s) 
        return ''.join(i for i in self.s[::-1])

class Queue :
    def __init__(self, q = None) :
        if q == None : self.q = []
        else         : self.q = q
    def enque(self, value) :
        return self.q.append(value)
    def deque(self) :
        if not self.isEmpty() :
            return self.q.pop(0)
        return -1
    def front(self) :
        return self.q[0]
    def rear(self) :
        return self.q[-1]
    def isEmpty(self) :
        return self.size() == 0
    def size(self) :
        return len(self.q)
    def __str__(self) :
        return ''.join(i for i in self.q)
        
if __name__ == '__main__' :
    color = input('Enter Input (Normal, Mirror) : ').split()
    mir, s1, s2, s3 = Queue(), Stack(), Stack(), Stack()
    [s1.push(i) for i in color[0]] 
    [s2.push(i) for i in color[1] ]
    # print(color[0][::-1]) # equal to color[0][-1::-1]
    # print(s1.s)
    # print(s2.s)
    loopAgain = [True, True]
    combo = [0, 0, 0]
    
    while loopAgain[1] :
        j = int()
        for i in range(s2.size() -1, 0, -1) :
            if i == j - 1 or i == j - 2 : 
                s2.pop()
                continue
            if s2.s[i] == s2.s[i - 1] == s2.s[i - 2] and (not s2.s[i] == s2.s[-1] or not i == 1) :
                j = i
                combo[1] += 1
                # print(f'\ttripple if\t{s2.s[i]}\tmir q \t{mir.q}', end='\t')
                mir.enque(s2.s[i])
                if s2.size() == 3 : 
                    s2.pop()
            else : s3.push(s2.s[i])
            s2.pop()
        [ s2.push(s3.pop()) for i in s3.s[::-1] ]
        for i in range(s2.size() -1, 0, -1) :
            if s2.s[i] == s2.s[i - 1] == s2.s[i - 2] :
                loopAgain[1] = True
                break
            else : loopAgain[1] = False
        if s2.size() <= 1 : break       

    c = mir.size() -1
    # print('!!!! mirror !!!!')
    i = 0
    mirB = Queue()
    while i in range(s1.size() -2) :
        if s1.s[i] == s1.s[i + 1] == s1.s[i + 2] and not mir.isEmpty():
            temp = mir.deque()
            mirB.enque(temp)
            s1.insert(i+2, temp) 
            i += 2
        else : i += 1
    i = 0
    while i in range(s1.size() - 2) : 
        if s1.s[i] == s1.s[i + 1] == s1.s[i + 2] :
            if not mirB.isEmpty() :
                # print(f' 123 : {s1.s[i]} == {mirB.q[0]}')
                if s1.s[i] == mirB.q[0]  : 
                    combo[2] += 1
                    mirB.deque()
                else    : combo[0] += 1
            else    : combo[0] += 1
            s1.pop(i)
            s1.pop(i)
            s1.pop(i)
            i -= 1
            if s1.size() == 3 : i = -1
        i += 1
        

    print('NORMAL :')
    print(s1.size())
    if s1.s == []   : print('Empty')
    else            : print(s1.__str__(1)) 
    print(f'{combo[0]} Explosive(s) ! ! ! (NORMAL)')
    if combo[2] > 0 : print(f'Failed Interrupted {combo[2]} Bomb(s)')

    print('------------MIRROR------------\n: RORRIM')
    print(s2.size())
    if s2.s == []   : print('ytpmE')
    else            : print(s2.__str__(0)) 
    print(f'(RORRIM) ! ! ! (s)evisolpxE {combo[1]}')


'''
Enter Input (Normal, Mirror) : AAABBBCDEE HHH
NORMAL :
8
EEDCAHAA
1 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
0
ytpmE
(RORRIM) ! ! ! (s)evisolpxE 1

Enter Input (Normal, Mirror) : AAABBBCDEE FGHHHIOPPP
NORMAL :
12
EEDCBHBBAPAA
0 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
4
FGIO
(RORRIM) ! ! ! (s)evisolpxE 2

Enter Input (Normal, Mirror) : AAABBBCDDDEE BBBTENETAAA
NORMAL :
5
EECBA
1 Explosive(s) ! ! ! (NORMAL)
Failed Interrupted 2 Bomb(s)
------------MIRROR------------
: RORRIM
5
TENET
(RORRIM) ! ! ! (s)evisolpxE 2

Enter Input (Normal, Mirror) : AAABBBDDD TENET
NORMAL :
0
Empty
3 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
5
TENET
(RORRIM) ! ! ! (s)evisolpxE 0

Enter Input (Normal, Mirror) : AAABBBCDDDEE OOOZZZTENETXXXYYY
NORMAL :
15
EEDZDDCBXBBAYAA
0 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
5
TENET
(RORRIM) ! ! ! (s)evisolpxE 4

/////////bug
Enter Input (Normal, Mirror) : DDDFFFGGG ABBBAACCC
NORMAL :
12
GAGGFBFFDCDD
0 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
0
ytpmE
(RORRIM) ! ! ! (s)evisolpxE 3

Enter Input (Normal, Mirror) : AJJJJJJJAA JJJJJJ
NORMAL :
0
Empty
2 Explosive(s) ! ! ! (NORMAL)
Failed Interrupted 2 Bomb(s)
------------MIRROR------------
: RORRIM
0
ytpmE
(RORRIM) ! ! ! (s)evisolpxE 2

Enter Input (Normal, Mirror) : PPPAAAABBBB PPPAAAA
NORMAL :
10
BAAPAAPAPP
1 Explosive(s) ! ! ! (NORMAL)
------------MIRROR------------
: RORRIM
1
A
(RORRIM) ! ! ! (s)evisolpxE 2


'''
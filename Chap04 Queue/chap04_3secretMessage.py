# Title       : Chapter : 4 - item : 3 - Secret Message

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
    def getQue(self) : # obj.q
        return self.q

def encodeMsg(word, key) :
    q1, q2, q3 = Queue(word), Queue(key), Queue()
    for i in range(q1.size()) :
        buff = q1.q[i]
        if 'A' <= buff <= 'Z' : buff = chr((ord(q1.q[i]) + q2.q[i] - 65) % 26 + 65)
        else                  : buff = chr((ord(q1.q[i]) + q2.q[i] - 97) % 26 + 97)
        # q2.enque(q2.deque()) # loop encode key
        # print(f'{i} : {q1.q[i]} -> {buff}')
        q3.enque(buff)
    return q3.q

def decodeMsg(wordEncode, key) :
    q1, q2, q3 = Queue(wordEncode), Queue(key), Queue()
    for i in range(q1.size()) :
        buff = q1.q[i]
        if 'A' <= buff <= 'Z' : buff = chr((ord(q1.q[i]) - q2.q[i] - 65) % 26 + 65)
        else                  : buff = chr((ord(q1.q[i]) - q2.q[i] - 97) % 26 + 97)
        # print(f'{i} : {q1.q[i]} -> {buff}')
        q3.enque(buff)
    return q3.q

if __name__ == '__main__' :
    s, n    = input('Enter String and Code : ').split(',')
    q1, q2  = Queue(), Queue()
    [q1.enque(i) for i in s if not i == ' '] 
    [q2.enque(int(n[i % len(n)])) for i in range(q1.size()) if q2.size() < q1.size()]
    # [q1.enque(i) for i in s if not i == ' '] 
    # [q2.enque(int(i)) for i in n]
    print(f'Encode message is :  {encodeMsg(q1.q, q2.q)}')
    print(f'Decode message is :  {decodeMsg(encodeMsg(q1.q, q2.q), q2.q)}')

'''
Enter String and Code : i love Python,256183
Encode message is :  ['k', 'q', 'u', 'w', 'm', 'S', 'a', 'y', 'n', 'p', 'v']
Decode message is :  ['i', 'l', 'o', 'v', 'e', 'P', 'y', 't', 'h', 'o', 'n']

Enter String and Code : KMITL,2
Encode message is :  ['M', 'O', 'K', 'V', 'N']
Decode message is :  ['K', 'M', 'I', 'T', 'L']

Enter String and Code : zzz zzz zzz,123456789
Encode message is :  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
Decode message is :  ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

Enter String and Code : I Love Data Structures But I Hate Bug,999997
Encode message is :  ['R', 'U', 'x', 'e', 'n', 'K', 'j', 'c', 'j', 'B', 'c', 'y', 'd', 'l', 'c', 'd', 'a', 'l', 'b', 'K', 'd', 'c', 'R', 'O', 'j', 'c', 'n', 'K', 'd', 'n']
Decode message is :  ['I', 'L', 'o', 'v', 'e', 'D', 'a', 't', 'a', 'S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 's', 'B', 'u', 't', 'I', 'H', 'a', 't', 'e', 'B', 'u', 'g']

Enter String and Code : SawaddeeKub,55555
Encode message is :  ['X', 'f', 'b', 'f', 'i', 'i', 'j', 'j', 'P', 'z', 'g']
Decode message is :  ['S', 'a', 'w', 'a', 'd', 'd', 'e', 'e', 'K', 'u', 'b']
'''
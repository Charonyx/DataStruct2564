# Title           : Chapter : 2 - item : 2 - weirdSubtract

def weirdSubtract(n, k) :
    for i in range(k) :
        if n % 10 == 0  : n //= 10
        else            : n -= 1
        # print(i)
    return n 

n, s = input('Enter num and sub : ').split()
print(weirdSubtract(int(n), int(s)))
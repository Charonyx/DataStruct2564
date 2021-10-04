# Title       : Chapter : 6 - item : 3 - POWER!

def power(n, p) :
    if p > 0    :
        # print(n,p)
        return n * power(n, p - 1)
    elif p == 0 :
        return 1

if __name__ == '__main__' :
    a, b = map(int, input('Enter Input a b : ').split())
    print(power(a, b))
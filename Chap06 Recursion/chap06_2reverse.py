# Title       : Chapter : 6 - item : 2 - Reverse Sort List

def reverse(numlist) :
    temp =[]
    if len(numlist) == 1    :
        return numlist
    else :
        # print('reverse')
        if numlist[0] > numlist[1]  : temp = [numlist[0]] + reverse(numlist[2:] + [numlist[1]])
        else                        : temp = [numlist[1]] + reverse(numlist[2:] + [numlist[0]])
        # print(temp)
    return reverse(temp[:-1]) + temp[-1:]     

if __name__ == '__main__' :
    num = list(map(int, input('Enter your List : ').split(',')))
    # print(num)
    print(f'List after Sorted : {reverse(num)}')
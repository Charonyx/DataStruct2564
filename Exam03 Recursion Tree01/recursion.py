def findMax(_list) :
    if len(_list) == 1 :
        return _list[0]
    else :
        _list2 = findMax(_list[1:])
        if  _list2 > _list[0] :
            return _list2
        else :
            return _list[0]

def power(b, p) :
    if p > 0 :
        return b * power(b, p-1)
    elif p == 0 :
        return 1

def rec_min(lst, acc_min=99999999):
    if len(lst) == 0:
        return acc_min
    else:
        num = lst.pop()
        if acc_min > num:
            acc_min = num
        return rec_min(lst, acc_min)

# if __name__ == '__main__':
#     lst = list(map(int, input("Enter Input : ").split()))
#     print(f'Min : {rec_min(lst)}')

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

# if __name__ == '__main__':
#     a,b = map(int, input('Enter Input : ').split())
#     if a == b == 0:
#         print('Error! must be not all zero.')
#         exit()
#     gcd = GCD(a, b)
#     if gcd < 0 and a < 0 and b < 0:
#         print(f'The gcd of {min(a, b)} and {max(a, b)} is : {- gcd}')
#     else:
#         print(f'The gcd of {max(a, b)} and {min(a, b)} is : {abs(gcd)}')

def length(txt):
    if txt[0:] is txt[-1:]:
        print(txt[0], end = "*")
        return 1
    s = length(txt[:-1])
    print(txt[s], end = "*" if s % 2 == 0 else "~")
    return s + 1

# if __name__ == '__main__':
#     print("\n",length(input("Enter Input : ")),sep="")

def rec_max(lst, acc_max=-99999999999):
    if len(lst) == 0:
        return acc_max
    else:
        num = lst.pop()
        if acc_max < num:
            acc_max = num
        return rec_max(lst, acc_max)


def rec_sort(lst, out, length):
    if len(out) < length:
        to_append = rec_max(lst.copy())
        # print(to_append)
        out.append(to_append)
        lst.remove(to_append)
        rec_sort(lst, out, length)
        if len(out) == length:
            return out
    else:
        return out


# if __name__ == '__main__':
#     lst = list(map(int, input('Enter your List : ').split(',')))
#     lst = rec_sort(lst, [], len(lst))
#     print(f"List after Sorted : {lst}")

# def reverse

# _input = list(map(int,(input('Enter list').split())))
# print(findMax(_input))

# print(power(2,5))


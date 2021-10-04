def reverse(numlist) :
    temp =[]
    if len(numlist) == 1    :
        return numlist
    else :
        print('wait')
        if numlist[0] > numlist[1] :
            temp = [numlist[0]] + reverse(numlist[2:] + [numlist[1]])
        else : 
            temp = [numlist[1]] + reverse(numlist[2:] + [numlist[0]])
            # return numlist[1] + reverse(num)
        # print(temp)
    return reverse(temp[:-1]) + temp[-1:]

def ssort(numlist) :
    temp =[]
    if len(numlist) <= 1    :
        return numlist
    # elif len(numlist) == 2  :
    #     return numlist if numlist[0] > numlist[1] else numlist[::-1]
    else :
        # print('----------ssort----------')
        # print(numlist[2:])
        # print(numlist[2::])
        if numlist[0] < numlist[1] :
            temp = [numlist[0]] + ssort([numlist[1]] + numlist[2:])
        else : 
            temp = [numlist[1]] + ssort([numlist[0]] + numlist[2:])
            # return numlist[1] + reverse(num)
        # print(temp)
        return ssort(temp[:-1]) + temp[-1:]

def bubble_sort(ar):
	if len(ar) <= 1:
		return ar
	# if len(ar) == 2:
	# 	return ar if ar[0] < ar[1] else [ar[1], ar[0]]
	a, b = ar[0], ar[1]
	bs = ar[2:]
	res = []
	if a < b:
		res = [a] + bubble_sort([b] + bs)
	else:
		res = [b] + bubble_sort([a] + bs)
	# Recursively call for the list
	# less than the last element and
	# and return the newly formed list
	return bubble_sort(res[:-1]) + res[-1:]
# Driver Code
# arr = [1, 3, 4, 5, 6, 2]
# res = bubble_sort(arr)
# print(*res)

if __name__ == '__main__' :
    num = list(map(int, input('Enter Input : ').split(',')))
    print(num)
    print(bubble_sort(num))
    print(ssort(num))
    print(reverse(num))
# ===================== Bubble Sort ======================
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr
if __name__ == '__main__' :
    _input = list(map(int, input('Enter Input : ').split()))
    print(_input)
    print(bubble_sort(_input))

# ===================== Selection Sort ======================
def selection(list) :
    for last in range(len(list) -1, -1, -1) :

        # if list[last] < 0 :
        #     continue
        
        max = list[0]
        maxIndex = 0
        for i in range(1, last + 1) :
           if list[i] > max :               # Ascending
               max = list[i]
               maxIndex = i
        # Swap max and last
        list[last], list[maxIndex] = list[maxIndex], list[last]
    print(*list)

# def selection_sort(arr):        
#     for i in range(len(arr)):
#         minimum = i
        
#         for j in range(i + 1, len(arr)):
#             # Select the smallest value
#             if arr[j] < arr[minimum]:
#                 minimum = j

#         # Place it at the front of the 
#         # sorted end of the array
#         arr[minimum], arr[i] = arr[i], arr[minimum]
            
#     return arr


# ===================== Insertion Sort ======================
def insertion(_word) :
    for i in range(1, len(_word)) :
        _temp = _word[i]                # insert element
        for j in range(i, -1, -1) :
            if _temp < _word[j - 1]   and j > 0 :
                _word[j] = _word[j - 1]
            else :
                _word[j] = _temp
                break
    return _word


# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i
        
#         while pos > 0 and arr[pos - 1] > cursor:
#             # Swap the number down the list
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         # Break and do the final swap
#         arr[pos] = cursor

#     return arr



# ===================== insertionRecursion Sort  ver 1 ======================

def insertionRecursion(array, n):
    # base case
    if n <= 1:
        return
    insertionRecursion(array, n-1)  # for bigger to small...

    last = array[n-1]   # store last value
    j = n - 2   # store before last index

    j = forLoopRecursion(array, j, last)     # for loop recursive

    array[j+1] = last   # assign last to the right position

    if len(array) != n:
        print(f'insert {last} at index {j+1} :', array[:n], array[n:])
    else:
        print(f'insert {last} at index {j+1} :', array)


def forLoopRecursion(array, j, last):
    # base case
    if j < 0 or array[j] < last:   # out of range and left is less than right
        return j

    array[j+1] = array[j]   # shift left position to right
    return forLoopRecursion(array, j-1, last)   # go left


lst = [int(i) for i in input('Enter Input : ').split()]

insertionRecursion(lst, len(lst))

print('sorted')
print(lst)





# ===================== Insertion Sort Recursion ver 2 ======================
def insertion_index(lst, curr_index, value):  # shift list value and return insertion index
    if curr_index > 0 and lst[curr_index - 1] > value:  # if this is not where to insert
        lst[curr_index] = lst[curr_index - 1]  # shift list element
        return insertion_index(lst, curr_index - 1, value)  # compare with another element
    else:
        return curr_index  # return insertion index


def insertion_sort(lst, start=0, length=None, progress=0):
    if length is None:  # for less parameters passing
        length = len(lst)

    value = lst[start]  # store value to be inserted

    index = insertion_index(lst, start, value)  # get insertion index and shift the list
    lst[index] = value  # insert value to the index
    progress += 1  # increase sorted part length

    if progress > 1:  # print insertion process (skip the first time)
        if len(lst[progress:]) != 0:  # prevent empty list printing '[]'
            print(f"insert {value} at index {index} : {lst[:progress]} {lst[progress:]}")
        else:
            print(f"insert {value} at index {index} : {lst[:progress]}")

    if start+1 < length:  # do until the last element
        insertion_sort(lst, start+1, length, progress)  # move to insert next element


if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    # Python function parameter is passed by reference, No return needed! Change will be applied directly.
    insertion_sort(in_lst)
    print("sorted")
    print(in_lst)




# ===================== Merge Sort ======================
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


# ===================== Quick Sort ======================
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)
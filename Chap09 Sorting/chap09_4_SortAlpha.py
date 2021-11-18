# Title       : Chapter : 9 - item : 4 - Sort by alphabet
# Question    : ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น
# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

def sortAlpha(list) :
    # print(f'list   : {list}')
    _alpha = dict()
    _word = []
    for i in list :
        for j in i :
            if 'a' <= j <= 'z' :
                _alpha[j] = _alpha.get(j, i)
                _word.append(j)
                break

    # print(f'alpha  : {_alpha}')
    # insertion
    for i in range(1, len(_word)) :
        _temp = _word[i]                # insert element
        for j in range(i, -1, -1) :
            if _temp < _word[j - 1]   and j > 0 :
                _word[j] = _word[j - 1]
            else :
                _word[j] = _temp
                break

    [print(_alpha[_word[i]], end=' ') for i in range(len(_word))]

if __name__ == '__main__' :
    _input = input('Enter Input : ').split()
    # print(_input)
    sortAlpha(_input)


'''
Enter Input : 932c 832u32 2344b
2344b 932c 832u32

Enter Input : 99a 78b c2345 11d
99a 78b c2345 11d

Enter Input : 572z 5y5 304q2
304q2 5y5 572z
'''
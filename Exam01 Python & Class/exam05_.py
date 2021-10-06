# Chapter : 12 - item : 5 - exam_python_1_2564_5a

class MyInt :
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) :
        return self.value

    def __add__(self, obj) :
        # print('add')
        # print(self.value)
        # print(obj.value * 2)
        # print(f'{self.value} + {(obj.value * 2)}')
        return self.value + obj.value + (self.value + obj.value)//2

    def toRoman(self) :
        _num = {"M" : 1000, "CM" : 900, "D" : 500, "CD" : 400, "C" : 100, "XC" : 90, "L" : 50, "XL" : 40, "X" : 10, "IX" : 9, "V" : 5, "IV" : 4, "I" : 1}
        _roman = ''
        # print(self.value, _num.get('M'))
        # print(_num.items())

        _temp = self.value
        # print(_temp)

        # print('========')
        for i, j in _num.items() :
            # print(i, j)
            while _temp >= j :
                _temp -= j
                _roman += i
        return _roman
        

if __name__ == '__main__' :
    print(' *** class MyInt ***')
    inp1, inp2 = [int(i) for i in input('Enter 2 number : ').split()]
    # print(inp1, inp2)
    # print(inp2*2)
    a = MyInt(inp1)
    b = MyInt(inp2)

    # print(a.toRoman())
    # print(b.toRoman())

    print(f'{inp1} convert to Roman : {a.toRoman()}')
    print(f'{inp2} convert to Roman : {b.toRoman()}')

    print(f'{inp1} + {inp2} = {a + b}')
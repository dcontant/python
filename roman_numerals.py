def romans_numerals(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += roman * (n // arabic)
        n %= arabic
    return result

if __name__ == '__main__':
    assert romans_numerals(1) == 'I', '1'
    assert romans_numerals(6) == 'VI', '6'
    assert romans_numerals(76) == 'LXXVI', '76'
    assert romans_numerals(499) == 'CDXCIX', '499'
    assert romans_numerals(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('all good')
    
    
def reverse_roman(roman_string):
    size = len(roman_string)
    roman_string +=  ' ' * (size%2)  # add a blank space if size is odd
    romans = {' ':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    for i in range(0, size, 2):
        x, y = roman_string[i: i+2]
        x, y = romans[x], romans[y]
        if x < y:
            ans += (y - x)
        else:
            ans += (x + y)
    return ans

if __name__ == '__main__':
    assert reverse_roman('I') == 1, '1'
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('all good');

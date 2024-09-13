def romans_numerals(n):
    ''' from  Checkio  '''
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

if __name__ == '__main__':
    assert romans_numerals(6) == 'VI', '6'
    assert romans_numerals(76) == 'LXXVI', '76'
    assert romans_numerals(499) == 'CDXCIX', '499'
    assert romans_numerals(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('all good')
    
    
def reverse_roman(roman_string):
    romans = {'':0,'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    ans = 0
    for i,digit in enumerate(roman_string):
        x,y = romans[digit],romans[roman_string[i+1:i+2]]
        if x < y:
            ans += romans[roman_string[i:i+2]]-romans[roman_string[i+1]]
        else:
            ans += x
    return ans

if __name__ == '__main__':
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('all good');

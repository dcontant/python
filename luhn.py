def luhn(purported):
    '''
    text and code from Wikipedia
    The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula 
    used to validate a variety of identification numbers, such as credit card numbers and canadian Social Insurance Numbers
    '''
    
    LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)  # sum_of_digits (index * 2)
    
    purported = str(purported)
    try:
        evens = sum(int(p) for p in purported[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(p)] for p in purported[-2::-2])
        return ((evens + odds) % 10 == 0)
    except ValueError:  # Raised if an int conversion fails
        return False
 
def luhn_checksum(data):
    check_digit = data[-1]
    data = ''.join(x for x in data[:-1] if x.isalpha() or x.isdigit())[::-1]
    total = 0
    for i,d in enumerate(data):
        if i%2 == 0:
            d = 2 * (ord(d) - 48)
            if d >= 10:
                d = int(str(d)[0]) +  int(str(d)[1])
        else:
            d = ord(d) - 48
        total += d
    return str((10 - total%10)%10) == check_digit


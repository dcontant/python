def hamming_distance(n, m):
    return bin(int(n) ^ int(m)).count('1')

if __name__ == '__main__':
    assert hamming_distance(117, 17) == 3, "First example"
    assert hamming_distance(1, 2) == 2, "Second example"
    assert hamming_distance(16, 15) == 5, "Third example"
    assert hamming_distance('16', '15') == 5
    print('all good')

''' 
from advent of code, show that the input of hashlib must be byte and not string thus .encode(endoding = 'utf-8')

also, beware repeat call to the same hashlib object m:  m.update(a); m.update(b) is equivalent to m.update(a+b).
'''
import hashlib
key = 'iwrupvqb'
for i in range(10**7):
    suffix = str(i)
    if hashlib.md5((key+suffix).encode(encoding='utf-8')).hexdigest()[:6] == '000000':
        print(i, hashlib.md5((key+suffix).encode(encoding='utf-8')).hexdigest())
    

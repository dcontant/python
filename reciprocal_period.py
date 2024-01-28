def period(n):
    '''return the period of the reciprocal of integer n,  from: https://www.hpmuseum.org/forum/newreply.php?tid=9818&replyto=101658'''
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    k, p = 0, 1
    if n == 1:
        return k
    while True:
        k += 1
        p = p * 10 % n
        if p == 1:
            return k


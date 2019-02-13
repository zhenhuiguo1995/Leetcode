
def myPow(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    if n == -1:
        return 1/x
    sign = n < 0
    temp = x
    while n != 1:
        if n%2 == 0:
            temp = temp ** 2
        else:
            temp = (temp ** 2) *x
        n //= 2
    if sign:
        return 1/temp
    return temp


print(myPow(2.0000, 10))
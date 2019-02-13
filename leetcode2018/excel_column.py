def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    string = ""
    while n > 26:
        r = n % 26
        n //= 26
        if r == 0:
            r = 26
            n -= 1
        string = chr(r + ord('A') -1) + string
    string = chr(n + ord('A') -1 ) + string
    return string
    
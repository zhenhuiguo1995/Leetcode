    def romanToInt(s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            if d[c] < d[p]:
                res = res - d[c]
            else:
                res += d[c]
                p = c
        return res
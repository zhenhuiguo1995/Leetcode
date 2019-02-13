def integer_to_roman(num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        a, b, c, d = 0, 0, 0, 0
        if num >= 1000:
            a = num // 1000
            num -= a * 1000
        if num >= 100:
            b = num // 100
            num -= b * 100
        if num >= 10:
            c = num // 10
            num -= c * 10
        if num >= 1:
            d = num // 1
            num -= c * 1
        return M[a] + C[b] + X[c] + I[d]
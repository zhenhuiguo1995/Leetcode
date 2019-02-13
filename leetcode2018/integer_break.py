import sys
def max_product(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
    else:
        return max(max_product(n-3)*3, max_product(n-4)*4)

def main():
    n = int(sys.argv[1])
    if n >= 4:
        return max_product(n)
    else:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2 

print(main())     
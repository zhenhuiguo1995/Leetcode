import sys

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    def helper(m, n):
        if m == 1 or n == 1:
            return 1
        else:
            return helper(m-1, n) + helper(m, n-1)
    print(helper(m,n))
main()
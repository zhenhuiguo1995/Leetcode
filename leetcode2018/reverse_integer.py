def reverse(x):
    list = []
    while x > 0:
        list.append(x%10);
        x = x // 10
    number = 0
    while len(list) > 0:
        number = number * 10 + list.pop(0)
    return number


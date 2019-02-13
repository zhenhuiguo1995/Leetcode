def shiftingLetters(S, shifts):
    temp = sum(shifts)
    total_shift = []
    pre = 0
    for i in shifts:
        temp -= pre
        total_shift.append(temp)
        pre = i
    string = ""
    for i in range(len(S)):
        string += chr(97 + (ord(S[i]) % 97 + total_shift[i]) % 26)        
    print(string)

S = 'z'
shifts = [52]
shiftingLetters(S, shifts)
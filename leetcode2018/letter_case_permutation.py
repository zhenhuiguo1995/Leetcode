def letter_case_permutation(S):
    res = [""]
    temp_1 = ""
    temp_2 = ""
    for letter in S:
        if letter.isdigit():            
            res = [i + letter for i in res]
        else:
            temp_1 = letter.lower()
            temp_2 = letter.upper()
            new = [i + temp_2 for i in res]
            res = [i + temp_1 for i in res] + new
    return res
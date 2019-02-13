def toLowerCase(str):
    """
    implement the lower function for string objects 
    """
    string = ""
    for letter in str:
        if letter >= 'A' and letter <= 'Z':
            string += chr(ord(letter) + 32)
        else:
            string += letter
    return string
    
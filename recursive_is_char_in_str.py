



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    m = aStr[len(aStr)//2]
    if m == char:
        return True
    if len(aStr) <= 1 or aStr == '':
        return False
    else:
        if m > char:
            return isIn(char, aStr[1,])
        if m < char:
            return isIn(char, aStr[,-1])
    return isIn(char, aStr)

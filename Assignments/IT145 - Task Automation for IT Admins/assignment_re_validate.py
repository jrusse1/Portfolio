import re
def isDateWithoutRE(text):
    if len(text) != 10:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[2] != '/':
        return False
    for i in range(3, 4):
        if not text[i]. isdecimal():
                return False
    if text[5] != '/':
        return False
    for i in range(6, 9):
        if not text[i].isdecimal():
            return False
    return True

print(isDateWithoutRE('10-21-2000'))
print(isDateWithoutRE('10/21/2000'))

dateRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
mo = dateRegex.search('11/15/2021')
print('Date found: ' + mo.group())

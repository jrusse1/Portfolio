import re
file = open('Phone_Number_and_Email_Address.txt')
lines = file.readlines()
phoneNumRegex = re.compile(r"\d\d\d\.\d\d\d\.\d\d\d\d")
emailRegex = re.compile(r':(.*@nostarch.com)')
counter = 0
for line in lines:
    try:
        mo = phoneNumRegex.findall(line)
        if len(mo) == 0:
            counter = 0
            continue
        elif len(mo) == 1:
            counter = 0
            print('Phone: ' + mo[counter])
        else:
            for i in range(len(mo)):
                print('Phone: ' + mo[counter])
                counter += 1
    except AttributeError:
        continue
for line in lines:
    try:
        mo = emailRegex.search(line)
        print('Email: ' + mo.group(1))
    except AttributeError:
        continue
import re
dateRegex = re.compile(r'(\d\d/)(\d\d/)(\d\d\d\d)')
mo = dateRegex.search('26/02/2021')
newDateFormat = mo.group(2) + mo.group(1) + mo.group(3)
print('New Date Format: ' + newDateFormat)
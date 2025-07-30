import json
numbers = []
favnum = int(input('What is your favorite number?\n'))
numbers.append(favnum)
filename = 'numbers.json'
with open (filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

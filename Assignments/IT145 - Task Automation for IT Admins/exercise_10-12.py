import json
filename = 'favnum.json'
try:
    with open(filename) as f_obj:
        favnum = json.load(f_obj)
except FileNotFoundError:
    favnum = input('What is your favorite number?\n')
    with open (filename, 'w') as f_obj:
        json.dump(favnum, f_obj)

print("I know your favorite number! It’s", favnum)
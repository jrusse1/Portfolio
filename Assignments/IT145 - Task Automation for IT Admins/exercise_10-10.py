try:
    with open('chamberjournal.txt') as cj:
        journal = cj.read()
    print('Amount of times "the" was found in Chamber Journal:', journal.lower().count('the'))
    with open('lavedette.txt') as lv:
        line = lv.read()
    print('Amount of times "the" was found in La Vedette:', line.lower().count('the'))
except FileNotFoundError:
    pass


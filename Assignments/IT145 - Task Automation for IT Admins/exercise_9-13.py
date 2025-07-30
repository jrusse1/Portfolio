from collections import OrderedDict

glossary = OrderedDict()
glossary['import'] = 'Used to borrow classes from a module'
glossary['ide'] = 'Environment used to create and test code'
glossary['list'] = 'Used to store multiple objects, like strings or integers.'
glossary['methods'] = 'Functions inside a class'
glossary['module'] = 'A file that contains a class to be called upon by another program'

for word, definition in glossary.items():
    print(word.title() + ": " + definition)

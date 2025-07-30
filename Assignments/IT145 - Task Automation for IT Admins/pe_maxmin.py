d = {'x':700, 'y':87, 'z': 57648488}

dmax = max(d.keys(), key=(lambda k: d[k]))
dmin = min(d.keys(), key=(lambda k: d[k]))

print('Maximum Value:', d[dmax])
print('Minimum Value:', d[dmin])


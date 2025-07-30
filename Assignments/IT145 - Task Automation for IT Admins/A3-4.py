def printinvites():
	index = 0
	for each in glist:
		print(glist[index] + ", would you like to come to dinner?")
		index = index + 1

glist = ['Jason Todd', 'Dick Grayson' , 'Bruce Wayne']
printinvites()

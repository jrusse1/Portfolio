def printinvites():
	index = 0
	for each in glist:
		print(glist[index] + ", would you like to come to dinner?")
		index = index + 1

glist = ['Jason Todd', 'Dick Grayson' , 'Bruce Wayne']
printinvites()

print ("-----------------------")
print (glist[0] , "can't make it. He was killed by the Joker... or was he?")


glist[0] = "Tim Drake"

printinvites()

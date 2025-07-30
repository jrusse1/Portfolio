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
	
print ("-----------------------")
print ("I've found a bigger table.")
glist.insert(0, "Barbara Gordon")
glist.insert(2, "Alfred Pennyworth")
glist.append("Damian Wayne")

printinvites()

print ("-----------------------")
print("I can only invite 2 people for dinner.")
removed = 0
for i in range(4):
	print (glist.pop(removed) + ", you've been uninvited to the dinner party.")

print ("-----------------------")
index = 0
for each in glist:
	print(glist[index] + ", you're still invited to dinner.")
	index = index + 1

for i in range(2):
	del glist[0]
print (glist)

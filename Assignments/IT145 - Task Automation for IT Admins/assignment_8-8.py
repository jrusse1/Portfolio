def make_album(artist, title):
	album = {artist:title}	
	print(album)

while True:
	artist = input("What is the artist? Type 'quit' to exit.\n")
	if artist == 'quit':
		break
	title = input("What is the album's title? Type 'quit' to exit.\n")
	if title == 'quit':
		break
	make_album(artist, title)


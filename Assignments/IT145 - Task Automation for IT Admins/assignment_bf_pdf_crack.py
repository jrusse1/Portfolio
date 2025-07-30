import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
with open('dictionary.txt', 'r') as dictionary:
    wordlist = [line.strip() for line in dictionary]

for i in wordlist:
    u = i.upper()
    encrypted = pdfReader.decrypt(u)
    if encrypted == 1:
        print('Found!\n', u)
        break
    else:
        print('Password incorrect: ', u)
        l = i.lower()
        encrypted = pdfReader.decrypt(l)
        if encrypted == 1:
            print('Found!\n', l)
            break
        else:
            print('Password incorrect: ', l)
        continue


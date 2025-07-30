alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789.$%/!@#'

def caesarEncrypt(plaintext, key):

    ciphertext = ''

    for p in plaintext:

        if p not in alphabet:
            continue

        index = alphabet.find(p)
        newIndex = index + key

        if newIndex > len(alphabet):
            newIndex = newIndex - len(alphabet)

        ciphertext += alphabet[newIndex]


    return ciphertext

def caesarDecrypt(plaintext, key):

    ciphertext = ''

    for p in plaintext:

        if p not in alphabet:
            continue

        index = alphabet.find(p)
        newIndex = index - key

        if newIndex > len(alphabet):
            newIndex = newIndex - len(alphabet)

        ciphertext += alphabet[newIndex]


    return ciphertext



ciphertext = caesarDecrypt('cx1@x! z5%41! 5@ x #e%1 $2 x @ay@#5#a#5$. z5%41! $! 9$.$x8%4xy1#5z z5%41! c41!1 1b1!e 81##1! 5. #41 91@@x31 5@ !1%8xz10 ye @$91 $#41! 81##1! 25d10 .a9y1! $2 %$@5#5$.@ 0$c. #41 x8%4xy1#q T41 .a9y1! $2 @452# %$@5#5$.@ 5@ #41 71e', 23)
print(ciphertext)


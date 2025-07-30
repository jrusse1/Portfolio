alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789.$%/!@#'

def caesarEncrypt(plaintext, key):

    ciphertext = ''

    for p in plaintext:

        if p not in alphabet:
            continue

        index = alphabet.find(p)
        newIndex = index + key

        if newIndex > len(alphabet) - 1:
            newIndex = newIndex - len(alphabet)
        elif newIndex < 0:
            newIndex = newIndex + len(alphabet)

        ciphertext += alphabet[newIndex]


    return ciphertext

def caesarDecrypt(plaintext, key):

    ciphertext = ''

    for p in plaintext:

        if p not in alphabet:
            continue

        index = alphabet.find(p)
        newIndex = index - key

        if newIndex > len(alphabet) - 1:
            newIndex = newIndex - len(alphabet)
        elif newIndex < 0:
            newIndex = newIndex + len(alphabet)

        ciphertext += alphabet[newIndex]


    return ciphertext



ciphertext = caesarEncrypt('#', 1)
print(ciphertext)


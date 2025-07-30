alphabet = "abcdefghijklmnopqrstuvwxyz0123456789.$%/!@#"


def caesarEncrypt(plaintext, key):
    ciphertext = ''

    counter = 0
    for p in plaintext:

        if p not in alphabet:
            ciphertext += p
            continue

        elif p in alphabet:
            counter += 1

            index = alphabet.find(p)

            if counter % 2:
                newIndex = index + key

            else:
                newIndex = index + (key + 2)

            if newIndex > len(alphabet) - 1:
                newIndex = newIndex - len(alphabet)
            elif newIndex < 0:
                newIndex = newIndex + len(alphabet)

            ciphertext += alphabet[newIndex]

    return ciphertext


def caesarDecrypt(plaintext, key):
    ciphertext = ''

    counter = 0
    for p in plaintext:

        if p not in alphabet:
            ciphertext += p
            continue

        elif p in alphabet:
            counter += 1

            index = alphabet.find(p)

            if counter % 2:
                newIndex = index - key

            else:
                newIndex = index - (key + 2)

            if newIndex > len(alphabet) - 1:
                newIndex = newIndex - len(alphabet)
            elif newIndex < 0:
                newIndex = newIndex + len(alphabet)

            ciphertext += alphabet[newIndex]

    return ciphertext

ciphertext = caesarDecrypt('j  n332zvp  4p03rzw  zo  4qp  lln3j2  ltysn2  5tuw  wz2  xjvn  4qp  lpj3n2  ltysn2  jy7 3nn32n   zwnn   4qp   j42llvn2   otwo   x52   lkz34   2sn   yn7   ltysn2   33ryp   2n6n21p nyptwpn2ryp lwo l2702lwlu91t1', 9)
print(ciphertext)


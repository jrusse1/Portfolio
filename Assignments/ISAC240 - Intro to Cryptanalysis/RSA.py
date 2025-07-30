
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def RSAencrypt(message):
    P1 = 11
    P2 = 13
    e = 7
    n = P1 * P2
    phiN = (P1 - 1) * (P2 - 1)
    d = int((6 * phiN + 1) / e)
    output = []
    decrypted = ''
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            c = index ** e % n
            output.append(c)
        else:
            output += letter
    for c in output:
        if c == ' ':
            decrypted += c
        else:
            m = int((c ** d) % n)
            decrypted += alphabet[m]
    return decrypted

print(RSAencrypt("This message is encrypted using RSA"))

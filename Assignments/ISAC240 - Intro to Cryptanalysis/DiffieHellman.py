def algorithm(p, g, alice, bob):

    A = (g ** alice) % p
    B = (g ** bob) % p

    aliceShared = (B ** alice) % p
    bobShared = (A ** bob) % p

    print('''Alice's shared key is: ''', aliceShared)
    print('''Bob's shared key is: ''', bobShared)

algorithm(17, 3, 15, 13)


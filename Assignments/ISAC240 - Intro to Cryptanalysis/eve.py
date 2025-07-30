import socket

HOST = "127.0.0.1"
ALICEPORT = 65431
BOBPORT = 65432
evePublicKey = (3 ** 11) % 17

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, ALICEPORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      alicePublicKey = conn.recv(1024)
      if not alicePublicKey:
        break
      print("Received Alice's Public Key: ", alicePublicKey)
      conn.sendall(str(evePublicKey).encode())
      sharedSecret = (int(alicePublicKey)**11) % 17
      print("Shared secret: ", sharedSecret)
  s.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, BOBPORT))
  s.sendall(str(evePublicKey).encode())
  bobPublicKey = s.recv(1024).decode()
  print("Received Bob's public key: ", bobPublicKey)
  sharedSecret = (int(bobPublicKey) ** 11) % 17
  print("Shared secret: ", sharedSecret)
  s.close()


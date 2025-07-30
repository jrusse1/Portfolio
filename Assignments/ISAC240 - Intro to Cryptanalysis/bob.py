import socket

HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      alicePublicKey = conn.recv(1024)
      if not alicePublicKey:
        break
      print("Received Alice's Public Key: ", alicePublicKey)
      bobPublicKey = (3**13) % 17
      conn.sendall(str(bobPublicKey).encode())
      sharedSecret = (int(alicePublicKey)**13) % 17
      print("Shared secret: ", sharedSecret)
  s.close()


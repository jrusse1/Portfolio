import socket

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  alicePublicKey = (3**15) % 17
  s.sendall(str(alicePublicKey).encode())
  bobPublicKey = s.recv(1024).decode()
  print("Received Bob's public key: ", bobPublicKey)
  sharedSecret = (int(bobPublicKey)**15) % 17
  print("Shared secret: ", sharedSecret)
  s.close()

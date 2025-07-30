import socket

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  alicePublicKey = (3**15) % 17
  s.sendall(str(alicePublicKey).encode())
  evePublicKey = s.recv(1024).decode()
  print("Received Eve's public key: ", evePublicKey)
  sharedSecret = (int(evePublicKey)**15) % 17
  print("Shared secret: ", sharedSecret)
  s.close()



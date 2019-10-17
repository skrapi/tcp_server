# Serial <-> TCP


import socket


TCP_IP = '178.128.160.227'

TCP_PORT = 9999


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

error =  s.connect((TCP_IP, TCP_PORT))
print(error)
s.settimeout(3)

print('Connected to: {}:{}'.format(TCP_IP, TCP_PORT))

while True:

  raw_input = input()
  s.send(raw_input.encode('utf-8'))


  return_data = s.recv(4)

  print(return_data.decode('utf-8'))


s.close()

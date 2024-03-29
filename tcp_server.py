import socket
import threading

bind_ip = '178.128.160.227'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
  while True:
    request = client_socket.recv(1024)
    print('Received {}'.format(request.decode('utf-8')))
    if request[:5] == 'close':      
      client_socket.send('CLSE'.encode('utf-8'))
      client_socket.close()
      break
    else:
      client_socket.send('ACK!'.encode('utf-8'))


  


while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()
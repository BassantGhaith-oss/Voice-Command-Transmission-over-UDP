import socket

client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

server_addr = (("192.168.5.1",5000))

client.sendto(b"Hello from UDP client",server_addr)

while True:
  data,addr = client.recvfrom(1024)

  print("Server: ", data.decode())

client.close()
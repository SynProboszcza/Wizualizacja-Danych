"""
def ciag(* liczby):
    suma = 0.0
    for x in range(len(liczby)):
        suma += liczby[x]
    print(suma)

ciag(float(range(1,15,1)))
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()

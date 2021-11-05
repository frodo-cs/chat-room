import socket as s
import variables as v
import threading

sockets = []

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
socket.bind((v.HOST, v.PORT))
socket.listen(v.CLIENTS)

print(f'Server on {v.HOST}:{v.PORT}')

# recibe el mensaje de un cliente
def message(socket): 
    try:
        msg = socket.recv(v.BUFFER_SIZE)
        if not len(msg):
            return False     
        return msg
    except:
        return False

# envia el mensaje a todos los clientes que no son el emisor
def broadcast(message, sock):
    for client in sockets:
        if client != sock:
            client.send(message)

# hilo del cliente
def socket_thread(conn, address):
    while True:
        msg = message(conn)
        if msg:
            broadcast(msg, conn)
        else:
            print("(%s, %s) is offline\n" % address)
            sockets.remove(conn)
            break
    conn.close()

# crea el hilo del cliente
def new_thread(conn, address):
    thread = threading.Thread(target = socket_thread, args=(conn, address, ))
    thread.start()
    return 

while True:
    conn, address = socket.accept()
    sockets.append(conn)
    print("(%s, %s) connected" % address)
    new_thread(conn, address)
    

import socket as s
import threading
import variables as v
import time

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((v.HOST,v.PORT))

# falta una para recibir mensajes del server
def received_data():
    while True:
        try:
            message = socket.recv(v.BUFFER_SIZE).decode('utf-8')
            print(message, end = '\n> ')
        except:
            socket.close()
            break

    
# enviar mensaje al server
def send_data():
    while True:
        try:
            msg = input(f'> ')
            if msg:
                message = msg.encode('utf-8')
                socket.send(message)
        except:
            socket.close()
            break

s_thread = threading.Thread(target = send_data)
s_thread.start()

r_thread = threading.Thread(target = received_data)
r_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    s_thread.join()
    r_thread.join()

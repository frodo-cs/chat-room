import socket as s
import threading
import variables as v

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((v.HOST,v.PORT))

# falta una para recibir mensajes del server
def received_data():
    while True:
        try:
            message = socket.recv(v.BUFFER_SIZE).decode('utf-8')
            print(message)
        except:
            print('Error')
            socket.close()

    
# enviar mensaje al server
def send_data():
    while True:
        try:
            msg = input(f'> ')
            if msg:
                message = msg.encode('utf-8')
                socket.send(message)
        except:
            print("Error")
            socket.close()
            break

s_thread = threading.Thread(target = send_data)
s_thread.start()

r_thread = threading.Thread(target = received_data)
r_thread.start()

import socket as s
import threading
import variables as v

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((v.HOST,v.PORT))

# falta una para recibir mensajes del server

# enviar mensaje al server
def send_data():
    while True:
        try:
            msg = input(f'> ')
            if msg:
                message = msg.encode()
                socket.send(message)
        except:
            print("Error")
            socket.close()
            break

s_thread = threading.Thread(target = send_data)
s_thread.start()

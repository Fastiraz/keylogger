# keylogger

```text
Just a simple keylogger that allow you to receive keylogs by sockets and log them in a text file.
```

> **Warning**
> It's not done, it's making a new connection to the server for each keystrokes. I have to optimize it.

This project is a simple keylogger that records keystrokes and sends them to a server.

---

## Requirements
- Python 3
- `pynput` library

---

## Installation
1. Clone the repository
2. Install the pynput library by running the command pip install pynput in your terminal

---

## Usage
1. Run server.py on the server computer
2. Run client.py on the client computer
3. The client program will start recording keystrokes and sending them to the server
4. The server will save the keystrokes in a log file named log.txt

--

## Explanation
**server.py**
The `server.py` file creates a socket and listens for incoming connections on port 12345. When a client connects, a new thread is started to handle that client's connection. The `instanceServeur` function is called in each thread to handle a single client connection.

The `instanceServeur` function receives the client socket and the client's information, such as IP address and port number. It then enters an infinite loop to receive messages from the client. Each message is decoded from bytes to a string and then saved to a log file named `log.txt`. If the message is "STOPIT" (in all caps), the function closes the client's socket and exits the loop.

**client.py**
The `client.py` file imports the `os` and `socket` modules and the `Listener` class from the `pynput.keyboard` module.

The `sender` function takes a message and sends it to the server. It creates a socket and connects to the server's IP address and port number. It then sends the message as bytes and closes the socket.

The `log_keystroke` function takes a `key` argument and converts it to a string. It also handles special cases for the space, shift, and enter keys, and then calls the `sender` function with the modified key.

The `Listener` class creates a new keyboard listener and calls the `log_keystroke` function whenever a key is pressed. The listener is started with the `l.join()` command.

---

## Conclusion
This keylogger is a simple demonstration of socket programming and keyboard monitoring in Python. While it can be used for legitimate purposes, it can also be used maliciously. It is important to use code responsibly and ethically.

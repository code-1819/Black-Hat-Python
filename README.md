---

# Black Hat Python by Justin Seitz AND Tim Arnold (Second Edition)

This repository consists of programs which are mainly provided inside the book mentioned above. Feel free to clone the repository and have fun!

## Requirements

- Python 3.x

## Description of the Programs

- ***tcp_client.py***: 
This script demonstrates a basic TCP client. It creates a socket object, connects to a specified target host and port, sends a simple HTTP GET request to Google's homepage, and then receives and prints the   response. 

- ***udp_client.py***: 
This script demonstrates a basic UDP client. It creates a socket object using UDP protocol, sends a simple message ("text_you_want") to a specified target host and port, and then receives and prints the response. 

- ***tcp_server.py***:
This script demonstrates a basic TCP server. It creates a socket object, binds it to a specified IP address and port, listens for incoming connections, and accepts client connections. Each client connection is handled in a separate thread by the `handle_client` function, which receives data from the client, prints it, and sends an acknowledgment back to the client.

- ***netcat.py***:
This script implements a basic Netcat-like tool in Python. It provides functionalities for connecting to a target host and port, listening for incoming connections, executing commands on the target, uploading files to the target, and interacting with a command shell. The script utilizes the `socket`, `subprocess`, and `threading` modules for network communication and command execution. It accepts various command-line arguments to specify the mode of operation, target IP address, port, and additional options such as command execution, file upload, and command shell interaction.

- ***proxy.py***:
This script is a lightweight Python script for creating a simple TCP proxy server. It allows users to intercept and modify network traffic between a client and a remote server. The script supports packet inspection, modification, and forwarding, providing a flexible tool for network debugging, monitoring, and security testing.

## License

This project is licensed under the [MIT License](LICENSE).

---

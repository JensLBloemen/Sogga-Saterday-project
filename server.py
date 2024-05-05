import socket
def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to an IP address and port
    server_address = ("192.168.8.115", 5555)
    sock.bind(server_address)

    clients = set()  # Keep track of client addresses

    
    try:
        print("Listining for clients...")
        while True:
            data, address = sock.recvfrom(4096)

            if address not in clients:
                print(f"New client: {address}")
                clients.add(address)  # Add new client to the set

            for client in clients:
                if client != address:  # Forward message to other clients
                    sock.sendto(data, client)
                    
    finally:
        sock.close()

if __name__ == '__main__':
    main()
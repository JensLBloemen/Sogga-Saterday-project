import socket
from player_pb2 import Player, Players  # Import your generated protobuf classes

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to an IP address and port
    server_address = ("127.0.0.1", 10000)
    sock.bind(server_address)

    clients = set()  # Keep track of client addresses

    print("Server is running and listening for clients...")
    
    try:
        while True:
            data, address = sock.recvfrom(4096)
            print(f"Received data from {address}")

            if address not in clients:
                clients.add(address)  # Add new client to the set

            for client in clients:
                if client != address:  # Forward message to other clients
                    sock.sendto(data, client)
                    print(f"Forwarded message to {client}")
                    
    finally:
        sock.close()

if __name__ == '__main__':
    main()
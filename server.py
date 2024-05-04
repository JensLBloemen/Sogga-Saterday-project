import socket
import player_pb2
import threading

def receive_player_info(server_socket, players, client_address):
    data, _ = server_socket.recvfrom(4096)
    print(f'Received {len(data)} bytes from {client_address}')

    # Parse the received protobuf message
    player = player_pb2.Player()
    player.ParseFromString(data)

    # Save player information
    players[player.id] = {'name': player.name, 'position': (player.position.x, player.position.y)}

    # Broadcast player information to all connected clients
    for addr, client_info in players.items():
        if addr != client_address:
            send_player_info(server_socket, player, client_info, addr)

def send_player_info(server_socket, new_player, client_info, client_address):
    # Create a Player message for the new player
    player_message = player_pb2.Player()
    player_message.id = new_player.id
    player_message.name = new_player.name
    player_message.position.x = new_player.position.x
    player_message.position.y = new_player.position.y

    # Create a Players message containing all player information
    players_message = player_pb2.Players()
    for addr, info in client_info.items():
        player = players_message.players.add()
        player.id = addr # addr == "name" klopt niet! -------------------------------------
        player.name = info['name']
        player.position.x = info['position'][0]
        player.position.y = info['position'][1]

    # Serialize Players message to send to the client
    data = players_message.SerializeToString()

    # Send the data to the client
    server_socket.sendto(data, client_address)

def handle_client(server_socket, players, client_address):
    while True:
        receive_player_info(server_socket, players, client_address)

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_address = ("127.0.0.1", 5555)
    print('Starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    players = {}
    threads = []

    try:
        while True:
            # Wait for a connection
            print('Waiting for a connection...')
            data, client_address = server_socket.recvfrom(4096)
            print(f'Connection from {client_address}')

            # Handle client in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(server_socket, players, client_address))
            client_thread.start()
            threads.append(client_thread)
    except KeyboardInterrupt:
        # Close all threads on KeyboardInterrupt
        for thread in threads:
            thread.join()
        print("Server stopped.")

if __name__ == '__main__':
    main()

import socket
import player_pb2
import threading

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ("127.0.0.1", 5555)
        self.server_socket.bind(self.server_address)
        self.players = {}
        self.threads = []



    def run(self):
        try:
            while True:
                print('Waiting for a connection...')
                data, client_address = self.server_socket.recvfrom(4096)
                self.client_address = client_address
                print(f'Received {len(data)} bytes from {client_address}')
                
                client_thread = threading.Thread(target=self.handle_client, args=(client_address,))
                client_thread.start()
                self.threads.append(client_thread)

        except KeyboardInterrupt:
            print('Server stopped')

    def handle_client(self, client_address):
        while True:
            self.receive_player_info(client_address)


    def receive_player_info(self, client_address):
        data, _ = self.server_socket.recvfrom(4096)
        print(f"{client_address=}, {data=}")
        print(f'Received {len(data)} bytes from {client_address}')

        # Parse the received protobuf message
        player = player_pb2.Player()
        player.ParseFromString(data)

        # Save player information
        self.players[client_address] = player

        # Broadcast player information to all connected clients
        for addr, player in self.players.items():
            if addr != client_address:
                self.send_player_info(player, client_address)

    def send_player_info(self, new_player, client_address):
    # Create a Player message for the new player
        player_message = player_pb2.Player()
        player_message.id = new_player.id
        player_message.name = new_player.name
        player_message.position.x = new_player.position.x
        player_message.position.y = new_player.position.y

        # Create a Players message containing all player information
        players_message = player_pb2.Players()
        data = players_message.SerializeToString()

        # Send the data to the client
        print(data, client_address)
        self.server_socket.sendto(data, client_address)

server = Server()
server.run()
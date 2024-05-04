import socket
import player_pb2

class Network:
    def __init__(self):
        self.server_address = ("127.0.0.1", 5555)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_player_info(self, player_id, player_name, position_x, position_y):
        # Create a Player message
        player = player_pb2.Player()
        player.id = player_id
        player.name = player_name
        player.position.x = position_x
        player.position.y = position_y

        # Serialize Player message to send to the server
        data = player.SerializeToString()

        # Send the data to the server
        self.server_socket.sendto(data, self.server_address)
        print('Player info sent to server')

    def receive_player_info(self):

        
        print('zabloing')
        # Receive player information from the server
        data, _ = self.server_socket.recvfrom(4096)
        print("zabloing2")
        # Parse the received protobuf message
        players_message = player_pb2.Players()
        players_message.ParseFromString(data)

        # Print received player information
        print("#", players_message)
        for player in players_message.players:
            print(f"Received Player Info: ID={player.id}, Name={player.name}, Position=({player.position.x}, {player.position.y})")

def main():
    """Test server connection."""

    network = Network()
    # Example usage: send player information to the server
    network.send_player_info(2, "Player 2", 20, 30)

    # Example usage: receive player information from the server
    network.receive_player_info()

if __name__ == '__main__':
    main()
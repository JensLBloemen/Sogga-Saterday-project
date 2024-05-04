import socket
import threading
from player_pb2 import Player  # Import your generated protobuf classes
import random

def listen_for_messages(sock):
    while True:
        data, _ = sock.recvfrom(4096)
        player = Player()
        player.ParseFromString(data)
        print(f"Received message: ID={player.id}, Name={player.name}, Position=({player.position.x}, {player.position.y})")

def send_messages(sock, server_address):
    player_id = random.randint(1, 5)
    while True:
        player = Player()
        player.id = player_id
        player.name = f"Player {player_id}"
        player.position.x = 10 + player_id
        player.position.y = 20 + player_id

        data = player.SerializeToString()
        sock.sendto(data, server_address)


        input("Press enter to send the next message...")

def main():
    server_address = ("192.168.8.115", 5555)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    receiver_thread = threading.Thread(target=listen_for_messages, args=(sock,))
    receiver_thread.start()

    send_messages(sock, server_address)

if __name__ == '__main__':
    main()
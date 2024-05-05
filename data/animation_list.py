import pygame
from classes.player import Player

animation_list = [pygame.transform.scale(
                        pygame.image.load(f"assets/hurt{i}.png"),
                        (Player.radius*2, Player.radius*2)) for i in range(4)] + \
                 [pygame.transform.scale(
                        pygame.image.load(f"assets/run{i}.png"),
                        (Player.radius*2, Player.radius*2)) for i in range(4)] +\
                 [pygame.transform.scale(
                        pygame.image.load(f"assets/shoot{i}.png"),
                        (Player.radius*2, Player.radius*2)) for i in range(4)] +\
                 [pygame.transform.scale(
                        pygame.image.load(f"assets/walk{i}.png"),
                        (Player.radius*2, Player.radius*2)) for i in range(4)]

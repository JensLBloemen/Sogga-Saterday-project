# --- game.py ----------------------------------------------------------------#
# Front end game loop, drawing objects and recieving player inputs.           #
# ----------------------------------------------------------------------------#

from classes.world import World
from classes.Arrow import Arrow
import numpy as np

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

pygame.init()

# --- Colors ------------------------------------------------------------------
#                Red    Green   Blue
BLACK =         (0,     0,      0)
RED =           (255,   0,      0)
BLUE =          (0,     0,      255)
WHITE =         (255,   255,    255)

# --- Settings ----------------------------------------------------------------

GAME_NAME = 'Game'
FPS = 60
WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 900

BACKGROUND_COLOR = BLACK

# --- Setup display -----------------------------------------------------------

display_centre = np.array([WINDOW_WIDTH/2, WINDOW_HEIGHT/2])
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

# --- Loop --------------------------------------------------------------------

class Game:

    def __init__(self, name) -> None:
        self.world = World()
        self.player = self.world.add_player(200, 200, name)

    def quit(self) -> None:
        """ Quit Game. """
        pygame.quit()
        quit()

    def draw(self) -> None:

        # Draw Player object in centre of frame.
        pygame.draw.circle(self.game_display, RED, (display_centre[0], display_centre[1]), self.player.radius)
        
        # Draw arrows.
        for arrow in self.world.arrows:
            relative_pos = arrow.pos - self.player.pos + display_centre
            pygame.draw.line(self.game_display, RED, (relative_pos[0], relative_pos[1]),
                             (relative_pos[0] - arrow.direction[0] * arrow.length, relative_pos[1] - arrow.direction[1]*arrow.length))

        # Draw other players and arrows.

        for id, player in self.world.other_players.items():
            relative_pos = player.pos - self.player.pos + display_centre
            pygame.draw.circle(self.game_display, BLUE, (relative_pos[0], relative_pos[1]), player.radius)

            # Draw arrows.

            for arrow in player.arrows:
                relative_pos = arrow.pos - self.player.pos + display_centre
                pygame.draw.line(self.game_display, WHITE, (relative_pos[0], relative_pos[1]), 
                                 (relative_pos[0] - arrow.direction[0]*arrow.length, relative_pos[1] - arrow.direction[1]*arrow.length))

        # Draw fixtures.
        for fixture in self.world.fixtures:
            relative_pos = fixture.pos - self.player.pos + display_centre
            fixt_rect = (relative_pos[0], relative_pos[1], 
                         fixture.width, fixture.height)
            pygame.draw.rect(self.game_display, BLUE, fixt_rect)

    def update(self) -> None:
        """ Draw new frame. """
        self.game_display.fill(BACKGROUND_COLOR)
        self.draw()
        self.world.update()
        pygame.display.update()
        clock.tick(FPS)

    def run(self) -> None:
        """ Main gameplay loop. """
    
        # Set up display
        self.game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Loop
        power = 0
        max_speed = 25

        while True:

            if pygame.mouse.get_pressed()[0]:                
                power += 1
            # Quit and close game by pressing the X right above..
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break

                
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    direction = np.array([x, y]) - display_centre
                    direction = direction / np.linalg.norm(direction)

                    speed = int(max_speed * (2 / (1 + np.exp(-power / 30)) - 1))

                    if speed > 5:
                        self.world.add_arrow(self.player.pos[0], self.player.pos[1], direction, speed)
    
                    print("Released mouse button. with speed = ", speed)
                    power = 0


            # Recieve arrow input controlls and call player to move.
            keys = pygame.key.get_pressed()
            x_vel = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
            y_vel = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
            self.world.move_player(np.array([x_vel, y_vel]))

            self.update()


        
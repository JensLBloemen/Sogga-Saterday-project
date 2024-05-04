# --- game.py ----------------------------------------------------------------#
# Front end game loop, drawing objects and recieving player inputs.           #
# ----------------------------------------------------------------------------#

from classes.world import World

import numpy as np
import pygame
pygame.init()

# --- Colors ------------------------------------------------------------------
#                Red    Green   Blue
BLACK =         (0,     0,      0)
RED =           (255,   0,      0)
BLUE =          (0,     0,      255)

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

    def __init__(self) -> None:
        self.world = World()
        self.player = self.world.add_player(0, 0)

    def quit(self) -> None:
        """ Quit Game. """
        pygame.quit()
        quit()

    def draw(self) -> None:

        # Draw Player object in centre of frame.
        pos = display_centre
        pygame.draw.circle(self.game_display, RED, (pos[0], pos[1]), self.player.radius)

        for id, player in self.world.other_players.items():
            relative_pos = player.pos - self.player.pos + display_centre
            pygame.draw.circle(self.game_display, BLUE, (relative_pos[0], relative_pos[1]), player.radius)

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
        while True:

            # Quit and close game by pressing the X right above..
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    self.quit()
                    break

            # Recieve arrow input controlls and call player to move.
            keys = pygame.key.get_pressed()
            x_vel = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
            y_vel = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
            self.world.move_player(np.array([x_vel, y_vel]))

            self.update()


        
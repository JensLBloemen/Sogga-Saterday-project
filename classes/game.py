# --- game.py ----------------------------------------------------------------#
# Front end game loop, drawing objects and recieving player inputs.           #
# ----------------------------------------------------------------------------#

from classes.world import World
from classes.Arrow import Arrow
from classes.animation import Animation
from data.animation_list import animation_list

import numpy as np
import math
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

        self.run_anim = Animation('run', 7, self.player.radius, 4, True)
        self.shoot_anim = Animation('shoot', 50, self.player.radius, 3, False)
        self.curr_animation = self.run_anim # miss copy ofzo

        self.mouse_x = 0
        self.mouse_y = 0

        self.arrow = pygame.transform.scale(pygame.image.load(f"assets/arrow.png"),
                        (self.player.radius*2, self.player.radius*2))

    def quit(self) -> None:
        """ Quit Game. """
        pygame.quit()
        quit()

    def draw(self) -> None:

        # Draw Player object in centre of frame.
        # pygame.draw.circle(self.game_display, RED, (display_centre[0], display_centre[1]), self.player.radius)
        [x, y] = np.array([self.x, self.y]) - display_centre
        angle = math.degrees(math.atan2(self.mouse_y - y, self.mouse_x - x))
        self.player.rotation = angle
        self.curr_animation.draw(self.game_display, display_centre[0], display_centre[1], -angle+90)

        # Draw arrows.
        for arrow in self.world.arrows:
            relative_pos = arrow.pos - self.player.pos + display_centre
            rotation = math.degrees(math.atan2(arrow.direction[0], arrow.direction[1]))
            rotated_image = pygame.transform.rotate(self.arrow, rotation)
            new_rect = rotated_image.get_rect(center=tuple(relative_pos))
            self.game_display.blit(rotated_image, new_rect.topleft)

        # Draw other players and arrows.
        for id, player in self.world.other_players.items():
            relative_pos = player.pos - self.player.pos + display_centre

            rotated_image = pygame.transform.rotate(animation_list[player.anim_id], -player.rotation+90)
            new_rect = rotated_image.get_rect(center=(relative_pos[0], relative_pos[1]))
            self.game_display.blit(rotated_image, new_rect.topleft)

            # pygame.draw.circle(self.game_display, BLUE, (relative_pos[0], relative_pos[1]), player.radius)

            # Draw arrows.
            for arrow in player.arrows:
                relative_pos = arrow.pos - self.player.pos + display_centre
                rotation = math.degrees(math.atan2(arrow.direction[0], arrow.direction[1]))
                rotated_image = pygame.transform.rotate(self.arrow, rotation)
                new_rect = rotated_image.get_rect(center=tuple(relative_pos))
                self.game_display.blit(rotated_image, new_rect.topleft)

        # Draw fixtures.
        for fixture in self.world.fixtures:
            relative_pos = fixture.pos - self.player.pos + display_centre
            fixt_rect = (relative_pos[0], relative_pos[1], 
                         fixture.width, fixture.height)
            pygame.draw.rect(self.game_display, BLUE, fixt_rect)
        


    def update(self, time) -> None:
        """ Draw new frame. """
        self.game_display.fill(BACKGROUND_COLOR)
        self.draw()
        self.world.update()
        self.curr_animation.update(time)
        self.player.anim_id = self.curr_animation.current_frame + ["hurt", "run",  "shoot" , "walk"].index(self.curr_animation.name) * 4

        pygame.display.update()
        clock.tick(FPS)

    def run(self) -> None:
        """ Main gameplay loop. """
    
        # Set up display
        self.game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Loop
        power = 0
        max_speed = 25

        time = 0
        while True:
            self.x, self.y = pygame.mouse.get_pos()

            # Draw arrow.
            if pygame.mouse.get_pressed()[0]:                
                power += 1
                self.curr_animation = self.shoot_anim

            # Quit and close game by pressing the X right above..
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break

                # Draw arrow, last update time.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.shoot_anim.last_update = time

                # Shoot arrow.
                if event.type == pygame.MOUSEBUTTONUP:
                    direction = np.array([self.x, self.y]) - display_centre
                    direction = direction / np.linalg.norm(direction)

                    speed = min(power/4, 25)

                    if power > 50:
                        self.world.add_arrow(self.player.pos[0], self.player.pos[1], direction, speed)
    
                    print("Released mouse button. with speed = ", speed)
                    power = 0
                    self.shoot_anim.current_frame = 0
                    self.shoot_anim.last_update = time
                    self.curr_animation = self.run_anim


            # Recieve arrow input controlls and call player to move.
            keys = pygame.key.get_pressed()
            x_vel = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
            y_vel = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
            self.world.move_player(np.array([x_vel, y_vel]))

            self.update(time)
            time +=1



        
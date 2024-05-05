import pygame

class Animation:

    def __init__(self, name : str, tpf : int, radius : int) -> None:
        self.radius = radius
        self.frames = [pygame.transform.scale(
                        pygame.image.load(f"../assets/{name}{i}.png"),
                        (self.radius*2, self.radius*2)) for i in range(4)]
        self.current_frame = 0
        self.last_update = 0
        self.frame_duration = tpf

    def draw(self, screen, x, y):
        # pygame.draw.circle(screen, (255,0,0), (x,y), self.radius)
        screen.blit(self.frames[self.current_frame], (x - self.radius, y-self.radius))
        

    def update(self, time):
        if time - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = time

# test.
if __name__ == "__main__":

    from pygame.locals import *

    # Initialize Pygame
    pygame.init()

    # Set screen dimensions
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Animation Example')

    # Create an Animation instance
    animation = Animation('shoot', 40, 60) 

    # Set up the game loop
    clock = pygame.time.Clock()
    running = True
    time = 0
    while running:
        
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update animation
        # current_time = pygame.time.get_ticks()
        animation.update(time)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the animation
        animation.draw(screen, 100, 100)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)
        time += 1

    # Quit Pygame
    pygame.quit()

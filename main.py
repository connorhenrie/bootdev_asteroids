import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    #initalize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #clock module
    clock = pygame.time.Clock()
    dt = 0.0

    #game loop
    while True:
        log_state()
        #quits program when window closes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

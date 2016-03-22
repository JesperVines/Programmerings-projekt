import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARK_RED = (120, 0, 0)
DARK_BLUE = (0, 0, 120)
DARK_GREEN = (0, 120, 0)


def draw_tree(screen, x, y):

    pygame.draw.rect(screen, DARK_RED, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, DARK_GREEN, [[150+x, 170+y], [75+x, 20+y], [x, 170+y]])
    pygame.draw.polygon(screen, DARK_GREEN, [[140+x, 120+y], [75+x, y], [10+x, 120+y]])


def main():

    pygame.init()

    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

    pygame.display.set_caption("itle screen")

    done = False

    clock = pygame.time.Clock()

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                done = True

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        screen.fill(DARK_BLUE)

        font = pygame.font.SysFont('Times New Roman', 100, True, False)
        text = font.render("Title goes here", True, BLACK)
        screen.blit(text, [375, 125])

        pygame.draw.circle(screen, WHITE, [100, 350], 20)
        pygame.draw.circle(screen, WHITE, [100, 475], 20)
        pygame.draw.circle(screen, WHITE, [100, 600], 20)

        font = pygame.font.SysFont('Times New Roman', 50, True, False)

        text = font.render("Play game", True, BLACK)
        screen.blit(text, [150, 325])

        text = font.render("Options", True, BLACK)
        screen.blit(text, [150, 450])

        text = font.render("Credits", True, BLACK)
        screen.blit(text, [150, 575])

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

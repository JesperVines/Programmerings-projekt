import Rooms
import pygame


def main():

    room_list = Rooms.rooms()

    current_room = room_list[0]

    pygame.init()

    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

    pygame.display.set_caption("The room")

    done = False

    clock = pygame.time.Clock()

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                done = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    next_room = room_list[current_room][1]
                    if next_room is None:
                        continue

                    current_room = next_room

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:

                    next_room = room_list[current_room][2]
                    if next_room is None:
                        continue

                    current_room = next_room

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:

                    next_room = room_list[current_room][3]
                    if next_room is None:
                        continue

                    current_room = next_room

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    next_room = room_list[current_room][4]
                    if next_room is None:
                        continue

                    current_room = next_room

        img = pygame.image.load(current_room[5])
        screen.blit(img, (0, 0))

        pygame.display.flip()

    clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

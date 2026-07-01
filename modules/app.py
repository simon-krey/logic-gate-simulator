import pygame

from modules.simulation import Simulation
from modules.storage import save_to_file, load_from_file

from modules.ui import Label

class App:
    def __init__(self):
        self.simulation = Simulation()
        self.running = False

    def render(self):
        pass

    def run(self):
        pygame.init()
        pygame.font.init()

        self.running = True

        test_label = Label((300, 300), (0, 0), "Netanjahu")

        display = pygame.display.set_mode((1000, 1000))
        screen = pygame.Surface((1000, 1000))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))

            test_label.render(screen)

            pygame.display.flip()

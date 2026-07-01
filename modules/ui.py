import pygame

class UIElement:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.color = (66, 135, 245)

    def update(self):
        pass

    def render(self, screen):
        pass

class Label(UIElement):
    def __init__(self, pos, size, text):
        super().__init__(pos, size)

        self.text = text
        self.font = pygame.font.Font(None, 20)
    
    def update(self):
        super().update()
    
    def render(self, screen: pygame.Surface):
        super().render(screen)

        screen.blit(self.font.render(self.text, True, self.color), self.pos)

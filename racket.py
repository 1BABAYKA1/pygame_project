import pygame
from colors import *
from directions import *


class Racket(pygame.sprite.Sprite):

    def __init__(self, screen, width, height, side):
        super().__init__()

        self.width, self.height = width, height

        self.racket_height = 100
        self.movement_speed = 20

        offset = 20

        self.screen = screen

        self.image = pygame.Surface([10, self.racket_height])
        self.image.fill(WHITE)

        pygame.draw.rect(self.image, WHITE, [0, 0, 10, self.racket_height])

        self.rect = self.image.get_rect()

        print(side)

        if side is Directions.LEFT:
            self.position = (offset, self.height / 2)

        else:
            self.position = (self.width - offset - 10, self.height / 2)

    @property
    def position(self):
        return (self.rect.x, self.rect.y)

    @position.setter
    def position(self, pos):
        try:
            pos_x, pos_y = pos

        except ValueError:
            raise ValueError("Pass an iterable with two items")

        else:
            self.rect.x, self.rect.y = pos_x, pos_y

    def move_up(self):

        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - self.movement_speed)

    def move_down(self):

        if self.position[1] + self.racket_height < self.height:
            self.position = (self.position[0], self.position[1] + self.movement_speed)

    def figni(self, screen, width, height, side):
        self.width, self.height = width, height

        self.figni_height = 15

        offset = 20

        self.screen = screen

        self.image = pygame.Surface([10, self.figni_height])
        self.image.fill(WHITE)

        pygame.draw.rect(self.image, WHITE, [0, 0, 10, self.figni_height])

        self.rect = self.image.get_rect()

        if side is Directions.LEFT:
            self.position = (offset, self.height / 2)

        else:
            self.position = (self.width - offset - 10, self.height / 2)



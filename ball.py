import pygame
import random
from colors import *
from directions import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, width, height):
        super().__init__()

        self.width, self.height = width, height

        self.direction = random.choice([Directions.DOWN_LEFT, Directions.DOWN_RIGHT, Directions.UP_LEFT, Directions.UP_RIGHT])

        self.screen = screen
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)

        pygame.draw.rect(self.image, WHITE, [0, 0, 10, 10])

        self.rect = self.image.get_rect()

        self.position = (width / 2 + 2, height / + 2)

        self.hits = 0

        self.speed_up = 1.0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def hit(self):
        self.hits += 1

        self.speed_up = 1.0+self.hits/10

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

    def up_left(self):

        self.position = (self.position[0] - 10*self.speed_up, self.position[1] - 10*self.speed_up)

    def up_right(self):

        self.position = (self.position[0] + 10*self.speed_up, self.position[1] - 10*self.speed_up)

    def down_left(self):

        self.position = (self.position[0] - 10*self.speed_up, self.position[1] + 10*self.speed_up)

    def down_right(self):

        self.position = (self.position[0] + 10*self.speed_up, self.position[1] + 10*self.speed_up)

    def update(self):
        if self.position[1] <= 10:  # upper border
            self.direction = random.choice(
                [Directions.DOWN_LEFT, Directions.DOWN_RIGHT])

        if self.position[1] >= self.height - 10:  # bottom border
            self.direction = random.choice(
                [Directions.UP_LEFT, Directions.UP_RIGHT])

        options = {Directions.UP_LEFT: self.up_left,
                   Directions.UP_RIGHT: self.up_right,
                   Directions.DOWN_LEFT: self.down_left,
                   Directions.DOWN_RIGHT: self.down_right,
                   }

        options[self.direction]()

    def toggle_direction(self):
        if self.direction == Directions.DOWN_LEFT:
            new_direction = Directions.DOWN_RIGHT

        if self.direction == Directions.DOWN_RIGHT:
            new_direction = Directions.DOWN_LEFT

        if self.direction == Directions.UP_RIGHT:
            new_direction = Directions.UP_LEFT

        if self.direction == Directions.UP_LEFT:
            new_direction = Directions.UP_RIGHT

        try:
            self.direction = new_direction
        except NameError:
            pass

    def get_x_val(self):
        return self.rect.x
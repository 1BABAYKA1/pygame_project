import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import pygame
from colors import *
from ball import Ball
from racket import Racket
from directions import Directions
from player import Player


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Project_KDMA')
        self.setFixedSize(360, 180)

        self.convert_button = QPushButton(self)
        self.convert_button.move(130, 0)
        self.convert_button.resize(100, 40)

        self.convert_button.setText('Choose your game')


        self.convert_button = QPushButton(self)
        self.convert_button.move(15, 90)
        self.convert_button.resize(130, 40)

        self.convert_button.setText('Snake')
        self.convert_button.clicked.connect(self.snake)

        self.convert_button = QPushButton(self)
        self.convert_button.move(195, 90)
        self.convert_button.resize(130, 40)

        self.convert_button.setText('Pinball')
        self.convert_button.clicked.connect(self.pinball)

        pygame.init()

        pygame.mixer.music.load('WYR_GEMI_-_Black_Samurai_67944226.mp3')
        pygame.mixer.music.play(-1, 0.0)

    def snake(self):
        os.startfile(r'""snake.exe""')

    def pinball(self):
        clock = pygame.time.Clock()

        WIN_WIDTH = 800
        WIN_HEIGHT = 640
        MAX_SCORE = 5

        DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
        pygame.init()
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode(DISPLAY, 0, 32)

        DONE = False
        FPS = 30

        left_player = Player(Directions.LEFT, 'Left')
        right_player = Player(Directions.RIGHT, 'Right')

        curr_ball = Ball(screen, WIN_WIDTH, WIN_HEIGHT)

        left_racket = Racket(screen, WIN_WIDTH, WIN_HEIGHT, Directions.LEFT)

        right_racket = Racket(screen, WIN_WIDTH, WIN_HEIGHT, Directions.RIGHT)

        rackets = pygame.sprite.Group()
        rackets.add(left_racket)
        rackets.add(right_racket)

        stuff_to_draw = pygame.sprite.Group()
        stuff_to_draw.add(left_racket)
        stuff_to_draw.add(right_racket)

        def game_over(screen, winner, left_paper, right_player):
            gray_overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            gray_overlay.fill(GRAY)
            gray_overlay.set_colorkey(GRAY)

            pygame.draw.rect(gray_overlay, BLACK, [0, 0, WIN_WIDTH, WIN_HEIGHT])

            gray_overlay.set_alpha(99)

            screen.blit(gray_overlay, (0, 0))

            font = pygame.font.SysFont(None, 100)
            game_over = font.render('{} Player WINS!'.format(winner.name), True, WHITE)

            screen.blit(game_over, (WIN_WIDTH / 2 - 300, WIN_HEIGHT / 2 - 100))

            scoreline = font.render(
                '{} - {}'.format(left_paper.score, right_player.score), True, WHITE)
            screen.blit(scoreline, (WIN_WIDTH / 2 - 50, WIN_HEIGHT / 2 + 100))

            pygame.display.update()

            pygame.time.delay(2000)

        while not DONE:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    DONE = True

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                DONE = True

            if keys[pygame.K_UP]:
                right_racket.move_up()

            if keys[pygame.K_DOWN]:
                right_racket.move_down()

            if keys[pygame.K_w]:
                left_racket.move_up()

            if keys[pygame.K_s]:
                left_racket.move_down()

            stuff_to_draw.update()
            curr_ball.update()

            col_left, col_right = curr_ball.rect.colliderect(left_racket.rect), curr_ball.rect.colliderect(
                right_racket.rect)
            if col_right == 1 or col_left == 1:
                curr_ball.toggle_direction()
                curr_ball.hit()

            if curr_ball.get_x_val() <= 0:  # left border
                right_player.score = 1
                curr_ball = Ball(screen, WIN_WIDTH, WIN_HEIGHT)

            elif curr_ball.get_x_val() >= WIN_WIDTH:  # right border
                left_player.score = 1
                curr_ball = Ball(screen, WIN_WIDTH, WIN_HEIGHT)

            # Print scores
            font = pygame.font.SysFont('Helvetica', 25)

            left_player_score = font.render(
                '{}'.format(left_player.score), True, (255, 255, 255))

            right_player_score = font.render(
                '{}'.format(right_player.score), True, (255, 255, 255))

            goal_text = font.render(
                '{}'.format(MAX_SCORE), True, (255, 255, 0))

            screen.blit(left_player_score, (WIN_WIDTH / 2 - 100, 10))
            screen.blit(right_player_score, (WIN_WIDTH / 2 + 100, 10))
            screen.blit(goal_text, (WIN_WIDTH / 2, 0))

            stuff_to_draw.draw(screen)
            curr_ball.draw(screen)

            if left_player.score >= MAX_SCORE:
                game_over(screen, left_player, left_player, right_player)

            elif right_player.score >= MAX_SCORE:
                game_over(screen, right_player, left_player, right_player)

            if left_player.score >= MAX_SCORE or right_player.score >= MAX_SCORE:
                DONE = True

            pygame.display.set_caption('Ping Pong ' + str(clock.get_fps()))

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
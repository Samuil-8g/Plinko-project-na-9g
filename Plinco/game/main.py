from ball import Ball
from board import *
from multis import *
from settings import *
from money import MoneyManager
import ctypes, pygame, pymunk, random, sys

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        self.money_manager = MoneyManager()

        # Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, 1800)

        # Plinko setup
        self.ball_group = pygame.sprite.Group()
        self.board = Board(self.space)

        # Debugging
        self.balls_played = 0

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                self.money_manager.handle_event(event)  # <-- Handle money input events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    mouse_pos = pygame.mouse.get_pos()

                    # Check if the mouse click position collides with the image rectangle
                    if self.board.play_rect.collidepoint(mouse_pos):
                        self.board.pressing_play = True
                    else:
                        self.board.pressing_play = False
                # Spawn ball on left mouse button release
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.board.pressing_play:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.board.play_rect.collidepoint(mouse_pos):
                        if self.money_manager.can_bet():  # <-- Only allow if player can bet
                            random_x = WIDTH//2 + random.choice([random.randint(-20, -1), random.randint(1, 20)])
                            click.play()
                            self.ball = Ball((random_x, 20), self.space, self.board, self.delta_time, self.money_manager)
                            self.ball_group.add(self.ball)
                            self.money_manager.deduct_bet()  # <-- Deduct bet when ball is played
                            self.board.pressing_play = False
                        else:
                            # Optionally, play an error sound or show a message
                            self.board.pressing_play = False
                    else:
                        self.board.pressing_play = False

            self.screen.fill(BG_COLOR)

            # Time variables
            self.delta_time = self.clock.tick(FPS) / 1000.0

            # Pymunk
            self.space.step(self.delta_time)
            self.board.update()
            self.ball_group.update()

            # Draw money manager UI
            self.money_manager.draw(self.screen)  # <-- Draw balance and bet boxes

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
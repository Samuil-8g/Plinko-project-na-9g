import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (100, 100, 255)

font = pygame.font.SysFont(None, 36)

balance = 150
bet = 10

main_box_rect = pygame.Rect(50, 50, 300, 150)
balance_box_rect = pygame.Rect(60, 70, 130, 50)
bet_box_rect = pygame.Rect(200, 70, 130, 50)

def draw_ui():
    pygame.draw.rect(screen, GREY, main_box_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, main_box_rect, 2, border_radius=10)

    pygame.draw.rect(screen, BLUE, balance_box_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, balance_box_rect, 2, border_radius=5)
    balance_text = font.render(f"Balance: ${balance}", True, WHITE)
    screen.blit(balance_text, (balance_box_rect.x + 10, balance_box_rect.y + 10))

    pygame.draw.rect(screen, BLUE, bet_box_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, bet_box_rect, 2, border_radius=5)
    bet_text = font.render(f"Bet: ${bet}", True, WHITE)
    screen.blit(bet_text, (bet_box_rect.x + 10, bet_box_rect.y + 10))

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_ui()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

import pygame
from settings import WIDTH, HEIGHT, BG_COLOR

class MoneyManager:
    def __init__(self, initial_balance=1000, initial_bet=10):
        self.balance = initial_balance
        self.bet = initial_bet
        self.font = pygame.font.SysFont(None, 40)
        self.input_active = False
        self.input_text = str(self.bet)
        # Move boxes to upper left and make them wider for large numbers
        self.input_rect = pygame.Rect(30, 80, 200, 48)
        self.balance_rect = pygame.Rect(30, 20, 300, 48)
        self.box_color = (100, 180, 220)  # New background color for boxes

        # All-in button
        self.all_in_rect = pygame.Rect(240, 80, 90, 48)
        self.all_in_color = (220, 120, 60)

    def draw(self, surface):
        # Draw balance box
        pygame.draw.rect(surface, self.box_color, self.balance_rect, border_radius=10)
        balance_text = self.font.render(f"Balance: ${self.balance:,}", True, (0, 0, 0))
        surface.blit(balance_text, (self.balance_rect.x + 16, self.balance_rect.y + 8))

        # Draw bet input box
        pygame.draw.rect(
            surface,
            self.box_color,
            self.input_rect,
            0,
            border_radius=10
        )
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            self.input_rect,
            2 if self.input_active else 1,
            border_radius=10
        )
        bet_text = self.font.render(f"Bet: ${self.input_text}", True, (0, 0, 0))
        surface.blit(bet_text, (self.input_rect.x + 16, self.input_rect.y + 8))

        # Draw All-in button
        pygame.draw.rect(surface, self.all_in_color, self.all_in_rect, border_radius=10)
        all_in_text = self.font.render("All In", True, (255, 255, 255))
        text_rect = all_in_text.get_rect(center=self.all_in_rect.center)
        surface.blit(all_in_text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.input_active = True
            else:
                self.input_active = False
            # All-in button click
            if self.all_in_rect.collidepoint(event.pos):
                self.bet = self.balance
                self.input_text = str(self.bet)
        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_RETURN:
                try:
                    bet = int(self.input_text)
                    if bet > 0 and bet <= self.balance:
                        self.bet = bet
                except ValueError:
                    pass
                self.input_active = False
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.unicode.isdigit():
                self.input_text += event.unicode
        # Live update bet if valid
        try:
            bet = int(self.input_text)
            if bet > 0 and bet <= self.balance:
                self.bet = bet
        except ValueError:
            pass

    def update_balance(self, multiplier):
        winnings = int(self.bet * multiplier)
        self.balance += winnings

    def deduct_bet(self):
        self.balance -= self.bet

    def can_bet(self):
        return self.bet > 0 and self.bet <= self.balance
import pygame
from pygame.sprite import Group
from ship import Ship
import pygame.font
pygame.init()

class Scoreboard():
    def __init__(self, ai_settings, screen, stat):
        self.ai_settings = ai_settings
        self.screen = screen
        self.stat = stat
        self.screen_rect = screen.get_rect()

        self.text_color = (0,0,10)
        self.font = pygame.font.SysFont(None, 26)

        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stat.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_str_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_str_img.get_rect()
        self.score_rect.right = self.screen_rect.right-10
        self.score_rect.top = 10

    def prep_high_score(self):
        rounded_high_score = int(round(self.stat.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_level(self):
        level_str = str(self.stat.level)
        self.level_str_img = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_str_img.get_rect()
        self.level_rect.right = self.screen_rect.right-10
        self.level_rect.top = 40

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stat.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)

    def draw_scoreboard(self):
        self.screen.blit(self.score_str_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.ships.draw(self.screen)

    def draw_level(self):
        self.screen.blit(self.level_str_img, self.level_rect)















        

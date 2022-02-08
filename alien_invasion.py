import sys
import pygame
import settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stat import GameStat
from button import Button
from scoreboard import Scoreboard

def run_game():

    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion created by Saif")
    ship = Ship(ai_settings, screen)
    aliens = Group()   
    bullets = Group()
    play_button = Button(ai_settings, screen, "Play")

    gf.create_fleet(ai_settings, screen, ship, aliens)
    stat = GameStat(ai_settings)
    sb = Scoreboard(ai_settings, screen, stat)
    #stat.game_active = True
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, aliens, stat, play_button, sb)
        if stat.game_active==True:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stat, sb)
            gf.update_aliens(ai_settings, screen, ship, bullets, aliens, stat, sb)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stat, play_button, sb)
        




run_game()

















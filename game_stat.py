import sys
import pygame

class GameStat():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        with open('scores.txt') as obj:
            content = obj.readlines()
            mx = 0
            for item in content:
                a = map(int, list(item.strip().split()))
                for x in a:
                    mx = max(mx, int(x))
        self.high_score = mx
        self.reset_stat()

    def reset_stat(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

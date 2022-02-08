class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 0.7
        self.ship_limit = 2

        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 300

        self.alien_speed_factor = 0.1 # 0.04
        self.fleet_drop_speed = 20
        self.fleet_direction = 1;

        self.speedup_scale = 1.1
        self.ship_speed_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1
        self.alien_points = 20

    def increase_speed(self):
        self.ship_speed_factor *= self.ship_speed_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)














        

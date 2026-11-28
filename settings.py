from pathlib import Path

class Settings:
    def __init__(self):
        self.score_path = Path.cwd() / 'Assets' / 'file'
        self.image_path = Path.cwd() / 'Assets' / 'images'
        self.sound_path = Path.cwd() / 'Assets' / 'sound'
        self.font_path = Path.cwd() / 'Assets' / 'fonts'
        self.name = 'Shootin` Space'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = self.image_path / 'pixel_space_background.png'
        # Aliens speed up faster each level than the ship does
        self.difficulty_scale = 1.15
        self.ship_difficulty_scale = 1.04
        self.scores_file = self.score_path / 'scores.json'

        self.ship_file = self.image_path / 'new_ship.png'
        self.ship_w = 40
        self.ship_h = 60

        self.bullet_file = self.image_path / 'blueLaserBlast.png'
        self.laser_sound = self.sound_path / 'pewpew_1.wav'
        self.impact_sound = self.sound_path / 'explosion.wav'

        self.alien_file = self.image_path / 'custom_alien_1.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.font_color = (255, 255, 255)
        self.button_font_size = 43
        self.HUD_font_size = 20
        self.font_file = self.font_path / 'Limelight' / 'Limelight-Regular.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 10
        self.starting_ship_count = 3

        self.bullet_w = 10
        self.bullet_h = 40
        self.bullet_speed = 15
        self.bullet_amount = 3

        self.alien_points = 50
        self.fleet_speed = 2
        self.fleet_drop_speed = 20

    def increase_difficulty(self):
        self.ship_speed *= self.ship_difficulty_scale
        self.bullet_speed *= self.ship_difficulty_scale
        self.fleet_speed *= self.difficulty_scale



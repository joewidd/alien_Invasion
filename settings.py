from pathlib import Path

class Settings:
    def __init__(self):
        self.score_path = Path.cwd() / 'Assets' / 'file'
        self.image_path = Path.cwd() / 'Assets' / 'images'
        self.sound_path = Path.cwd() / 'Assets' / 'sound'
        self.font_path = Path.cwd() / 'Assets' / 'fonts'
        self.name = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = self.image_path / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = self.score_path / 'scores.json'

        self.ship_file = self.image_path / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60

        self.bullet_file = self.image_path / 'blueLaserBlast.png'
        self.laser_sound = self.sound_path / 'laser.mp3'
        self.impact_sound = self.sound_path / 'impactSound.mp3'

        self.alien_file = self.image_path / 'enemy_4.png'
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
        self.ship_speed = 15
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 25
        self.bullet_amount = 5

        self.alien_points = 50
        self.fleet_speed = 7
        self.fleet_drop_speed = 40

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale



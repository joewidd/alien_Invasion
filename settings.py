from pathlib import Path

class Settings:
    def __init__(self):
        self.image_path = Path.cwd() / 'Assets' / 'images'
        self.sound_path = Path.cwd() / 'Assets' / 'sound'
        self.name = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = self.image_path / 'Starbasesnow.png'

        self.ship_file = self.image_path / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 15

        self.bullet_file = self.image_path / 'blueLaserBlast.png'
        self.laser_sound = self.sound_path / 'laser.mp3'
        self.bullet_speed = 25
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = self.image_path / 'enemy_4.png'
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.alien_w = 40
        self.alien_h = 40
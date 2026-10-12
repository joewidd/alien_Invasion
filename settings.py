from pathlib import Path

class Settings:
    def __init__(self):
        self.image_path = Path.cwd() / 'Assets' / 'images'
        self.name = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = self.image_path / 'Starbasesnow.png'

        self.ship_file = self.image_path / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 15
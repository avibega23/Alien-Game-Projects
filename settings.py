class Settings():
    "To Store All The Settings Of The Game"

    def __init__(self):
        '''Initiliazes The Game Settings'''
        #screen Settings
        self.ship_speed_factor = 1.5
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230,230,230)

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        
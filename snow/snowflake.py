__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"

import numpy as np
import pygame


class Snowflake:
    """
    Snowflake (for Christmas atmosphere :D )
    """
    def __init__(self, display_width, display_height):
        self.x = np.random.uniform(0, display_width)
        self.y = np.random.uniform(0, display_height)

        self.state = [pygame.image.load('snow/snowflake.png'), pygame.image.load('snow/snowflake_2.png'),
                      pygame.image.load('snow/snowflake_3.png'), pygame.image.load('snow/snowflake_4.png')]
        self.state_i = np.random.randint(0,4)
        self.img = self.state[self.state_i]

        self.size_x = self.get_random_size()
        self.size_y = self.size_x + 2
        self.img = pygame.transform.scale(self.img, (self.size_x, self.size_y))
        self.speed = np.zeros(2)
        self.gravity = np.array([0, 0.02 * self.size_x/10])
        self.acceleration = []
        self.angle = np.random.uniform() * 2*np.pi
        self.x_off = 0
        if np.random.uniform() > 0.5:
            self.direction = 1
        else:
            self.direction = -1

    def get_random_size(self):
        """
        Generates a random size of a snowflake
        :return: size
        """
        size = np.power(np.random.uniform(0, 1), 1)
        return int(size*24)

    def apply_force(self):
        pass

    def show(self, game_display):
        """
        Displays a snowflake
        :param game_display: pygame.game_display
        :return:
        """
        game_display.blit(self.img, (self.x, self.y))

    def update(self, display_width, display_height, wind):
        """
        Updates a position of the snowflake
        :param display_width: pygame.game_display
        :param display_height: pygame.game_display
        :param wind: wind force
        :return:
        """
        self.x_off = np.sign(self.angle) * self.size_x/10
        self.speed += self.gravity
        self.x =  self.x + self.x_off + wind[0]
        self.y = self.y + self.speed[1] + wind[1]
        self.angle += (self.direction * np.sqrt(self.speed[0]**2 + self.speed[1]**2))/1000

        if self.y > display_height or self.x > display_width:
            self.x_off = 0
            self.size_x = self.get_random_size()
            self.size_y = self.size_x + 2
            self.x = np.random.uniform(0, display_width)
            self.y = np.random.uniform(-display_height, 0)
            self.speed = np.zeros(2)
            self.img = pygame.image.load('snow/snowflake.png')
            self.img = pygame.transform.scale(self.img, (self.size_x, self.size_y))
            if np.random.uniform() > 0.5:
                self.direction = 1
            else:
                self.direction = -1



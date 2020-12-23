__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"

import numpy as np
from snow.snowflake import Snowflake


class Snow:
    """
    Snow is created by the list of snowflakes
    """
    def __init__(self, snowflakes_number, display_width, display_height):
        """
        Snow
        :param snowflakes_number:number of snowflakes
        :param display_width: pygame.game_display
        :param display_height: pygame.game_display
        """
        self.snowflakes = self.get_snowflakes(snowflakes_number, display_width, display_height)
        self.z_off = 0
        self.wx = np.random.uniform(-1, 1)
        self.wind = [self.wx, 0]

    def get_snowflakes(self, snowflakes_number, display_width, display_height):
        """
        Generates a list of snowflakes
        :param snowflakes_number: number of snowflakes
        :param display_width: pygame.game_display
        :param display_height: pygame.game_display
        :return:
        """
        snowflakes = []

        for i in range(snowflakes_number):
            snowflakes.append(Snowflake(display_width, display_height))

        return snowflakes

    def update(self, display_width, display_height):
        """
        Updates the snowflakes
        :param display_width: pygame.game_display
        :param display_height: pygame.game_display
        :return:
        """

        self.z_off += 0.1

        for i in range(len(self.snowflakes)):
            self.snowflakes[i].update(display_width, display_height, self.wind)

    def show(self, game_display):
        """
        Shows the snowflakes
        :param game_display: pygame.game_display
        :return:
        """
        for snowflake in self.snowflakes:
            snowflake.show(game_display)
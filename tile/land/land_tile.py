__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"

import pygame
from tile.tile import Tile


class LandTile(Tile):
    """
    Land tile
    """
    def __init__(self, x, y, land_number):
        super().__init__(x, y)
        self.type = 'land_tile'
        self.img = self.load_img(land_number)
        self.number = land_number

    def load_img(self, land_number=None):
        """
        Loads the image
        :param land_number: number corresponding with the tile
        :return:
        """
        if land_number:
            return pygame.image.load('winter_tile_set/PNG/land/land_'+str(land_number)+'.png')
        else:
            return pygame.image.load('winter_tile_set/PNG/land/land_' + str(self.number) + '.png')



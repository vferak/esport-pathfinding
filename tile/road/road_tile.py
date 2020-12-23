__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"

import pygame
from tile.tile import Tile


class RoadTile(Tile):
    """
    Road tile
    """
    def __init__(self, x, y, img_file_name):
        super().__init__(x, y)
        self.type = 'road'
        self.img_file_name = img_file_name
        self.img = pygame.image.load('winter_tile_set/PNG/road/'+self.img_file_name)
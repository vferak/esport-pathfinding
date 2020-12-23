import pygame
from abc import ABC


class Tile(ABC):
    """
    Abstract class for a tile
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 'land_tile'
        self.img = None
        self.img_file_name = None

    def set_draw_y(self):
        """
        Calculates the positions of the left-down corner
        :return:
        """
        self.draw_y = self.y + self.img.get_height()

    def show(self, game_display):
        """
        Shows a tile
        :param game_display: pygame.game_display
        :return:
        """
        try:
            game_display.blit(self.img, (self.x, self.y))
        except:
            pass

    def reset_img(self, img_file_name):
        """
        Resetting of the image of the tile
        :param img_file_name: file name of the image
        :return:
        """
        self.img_file_name = img_file_name
        self.img = pygame.image.load('winter_tile_set/PNG/' + self.type + '/' + img_file_name)

    def in_collision(self, tile_set):
        """
        If two tiles are in collision returns True, otherwise False
        :param tile_set: set of tiles
        :return: True if two tiles are in collision, False otherwise
        """
        for tile in tile_set:
            if tile != self:
                if self.is_inside(tile):
                    return True
                elif self.collision_y(tile):
                    if self.collision_x(tile):
                        return True
        return False

    def is_inside(self, tile):
        """
        Checks whether one tile is within another one
        :param tile: tile
        :return: True if a tile is within another one, False, otherwise
        """
        if self.y > tile.y and self.y+self.img.get_height() < tile.img.get_height():
            if self.x > tile.x and self.x+self.img.get_width() < tile.img.get_width():
                return True
        return False

    def collision_y(self, tile):
        """
        Checks a collision in vertical direction
        :param tile: tile
        :return:
        """
        if tile.y < self.y + self.img.get_height() < tile.y + tile.img.get_height() or \
                self.y < tile.y + tile.img.get_height() < self.y + self.img.get_height():
            return True

        return False

    def collision_x(self, tile):
        """
        Checks a collision in horizontal direction
        :param tile: tile
        :return:
        """
        if tile.x + tile.img.get_width() >= self.x >= tile.x or \
                tile.x <= self.x + self.img.get_width() <= tile.x + tile.img.get_width():
                    return True
        return False



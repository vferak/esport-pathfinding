__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"


import pygame


class Grid:
    """
    Grid for playground
    """
    def __init__(self, screen_width, screen_height, grid_size):
        self.grid = self.create_grid(screen_width, screen_height, grid_size)

    def create_grid(self, screen_width, screen_height, grid_size):
        """
        Generates a grid base don the grid_size
        :param screen_width: pygame.game_display
        :param screen_height: pygame.game_display
        :param grid_size: size a grid tile
        :return: grid
        """
        grid = []

        for x in range(screen_width // grid_size):
            row = []
            for y in range(screen_height // grid_size):
                rect = pygame.Rect(x * grid_size, y * grid_size, grid_size, grid_size)
                row.append(rect)
            grid.append(row)

        return grid

    def show_grid(self, game_display):
        """
        Displays a grid
        :param game_display: pygame.game_display
        :return:
        """
        for row in self.grid:
            for col in row:
                pygame.draw.rect(game_display, (192, 192, 192), col, 1)

    def get_grid_rect_pos(self, x, y):
        """
        Returns x and y coordinates of a grid tile if x and y belongs to this grid tile
        :param x: x-coordinate
        :param y: y-coordinate
        :return: grid_tile.x, grid_tile.y if this grid tile exists, None, None otherwise
        """
        for row in self.grid:
            for rect in row:
                if y >= rect.y and y <= rect.y + rect.height:
                    if x > rect.x and x < rect.x+rect.width:
                        return rect.x, rect.y
        return None, None

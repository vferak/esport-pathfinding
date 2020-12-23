__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"


import pygame
from tkinter import *
import json
from tile.land.land_tile import LandTile
from tile.road.road_tile import RoadTile
from tile.building.building import Building
from tile.decor.decor_tile import Decor
from tile.tile_matrix import TileMatrix
from utils.grid import Grid
from coin.coin import Coin
from coin.coin_matrix import CoinMatrix
from satyr.satyr import Satyr
from hero.hero import Hero
from snow.snow import Snow


class PygamePlayground:
    """
    Playground for a game.
    """
    def __init__(self, grid_size):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode()
        self.winter_tiles = None
        self.fill_winter()
        self.grid_size = grid_size
        self.width, self.height = self.game_display.get_size()
        self.grid = Grid(self.width, self.height, self.grid_size)
        self.imaginary_rectangle = None
        self.tiles = []
        self.road_matrix = TileMatrix(self.width, self.height, self.grid_size, self.grid_size)
        self.build_matrix = TileMatrix(self.width, self.height, self.grid_size, self.grid_size)
        self.decor_matrix = TileMatrix(self.width, self.height, self.grid_size, self.grid_size)
        self.game_state = 'Continue'
        self.coins_number = 1
        self.satyrs_number = 1
        self.snowflake_number = 1000
        self.coins = []  # List of coins
        self.satyrs = []  # List of satyrs
        self.hero = None  # Main hero
        self.snow = Snow(self.snowflake_number, self.width, self.height)
        self.coinMatrix = CoinMatrix()

    def create_object(self, x, y, type, img_file_name):
        """
        Creates an object based on type
        :param x: x-coordinate
        :param y: y-coordinate
        :param type: type - 'road', 'building', 'decor'
        :param img_file_name: file name of the corresponding image
        :return:
        """
        if type == 'road':
            return RoadTile(x, y, img_file_name)
        elif type == 'building':
            return Building(x, y, img_file_name)
        elif type == 'decor':
            return Decor(x, y, img_file_name)

    def position_occupied(self, x, y, type):
        """
        If a tile is occupied, returns True, otherwise, False
        :param x: x-coordinate
        :param y: y-coordinate
        :param type: type of the object
        :return: True if a tile is occupied, False otherwise
        """
        if type == 'road':
            return self.road_matrix.position_occupied(x, y)
        elif type == 'building':
            return self.build_matrix.position_occupied(x, y)
        elif type == 'decor':
            return self.decor_matrix.position_occupied(x, y)

    def add_tile_to_matrix(self, item):
        """
        Append a new tile (road, build, decor) to the playground (and corresponding matrix)
        :param item: road, build, or decor tile
        :return:
        """
        if item.type == 'road':
            self.road_matrix.add(item)
        elif item.type == 'building':
            self.build_matrix.add(item)
        elif item.type == 'decor':
            self.decor_matrix.add(item)

    def del_tile_from_matrix(self, item):
        """
        Removes a tile from the playground (and corresponding matrix)
        :param item:
        :return:
        """
        if item.type == 'road':
            self.road_matrix.del_item(item)
        elif item.type == 'building':
            self.build_matrix.del_item(item)
        elif item.type == 'decor':
            self.decor_matrix.del_item(item)

    def show_tile_from_matrix(self, type):
        """
        Display the objects
        :param type: 'road', 'building', 'decor'
        :return:
        """
        if type == 'road':
            self.road_matrix.show(self.game_display)
        elif type == 'building':
            self.build_matrix.show(self.game_display)
        elif type == 'decor':
            self.decor_matrix.show(self.game_display)

    def process_event(self, object_file_name, object_type):
        """
        Method for events processing
        :param object_file_name: name of image file corresponding to the selected toggle button
        :param object_type: type of the selected object (based on toggle button)
        :return:
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # For object creation, delete or regeneration
                if object_file_name is not None:
                    x, y = pygame.mouse.get_pos()
                    grid_rect_x, grid_rect_y = self.grid.get_grid_rect_pos(x, y)
                    occupied, occup_item = self.position_occupied(x, y, object_type)

                    if occupied:
                        self.del_tile_from_matrix(occup_item)
                    else:
                        item = self.create_object(grid_rect_x, grid_rect_y, object_type, object_file_name)
                        self.add_tile_to_matrix(item)

            elif event.type == pygame.KEYDOWN:
                # For save of the map
                if event.key == pygame.K_F5:
                    self.game_state = 'Save'
                # For load of the map -  filename: "my_tiles.json"
                elif event.key == pygame.K_F9:
                    self.game_state = 'Load'
                # For coins creation
                elif event.key == pygame.K_F10:
                    self.coins = [Coin(self.road_matrix), Coin(self.road_matrix)]
                    self.coinMatrix.updateCoins(self.coins)
                # For satyrs creation
                elif event.key == pygame.K_F11:
                    pass
                #For hero motion
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_F5 or event.key == pygame.K_F9:
                    self.game_state = 'Continue'

    def sort_objects_by_draw_y(self):
        """
        Objects must be sort based on y-coordinate for correct depiction.
        All objects must be processed here including coins and satyrs.
        :return:
        """
        tmp_objects = []

        for i in range(len(self.road_matrix.matrix)):
            for j in range(len(self.road_matrix.matrix[0])):
                if self.decor_matrix.matrix:
                    if self.decor_matrix.matrix[i][j] not in tmp_objects and self.decor_matrix.matrix[i][j] is not None:
                        self.decor_matrix.matrix[i][j].set_draw_y()
                        tmp_objects.append(self.decor_matrix.matrix[i][j])
                if self.build_matrix.matrix:
                    if self.build_matrix.matrix[i][j] not in tmp_objects and self.build_matrix.matrix[i][j] is not None:
                        self.build_matrix.matrix[i][j].set_draw_y()
                        tmp_objects.append(self.build_matrix.matrix[i][j])

        if self.satyrs:
            for satyr in self.satyrs:
                satyr.set_draw_y()
                tmp_objects.append(satyr)

        if self.coins:
            for coin in self.coins:
                coin.set_draw_y()
                tmp_objects.append(coin)

        if self.hero:
            self.hero.set_draw_y()
            tmp_objects.append(self.hero)

        if tmp_objects:
            tmp_objects = sorted(tmp_objects, key=lambda obj: obj.draw_y)

        return tmp_objects

    def draw_objects(self, my_objects):
        """
        Method of objects drawing
        :param my_objects: list of objects
        :return:
        """
        for object in my_objects:
            object.show(self.game_display)

    def update(self):
        """
        Method of update the game.
        :return:
        """
        if self.winter_tiles:
            for i in range(len(self.winter_tiles)):
                self.winter_tiles[i].show(self.game_display)
        self.grid.show_grid(self.game_display)  # Show a grid
        self.show_tile_from_matrix('road')

        # Sorting of the objects based on y-coordinates for correct depiction
        tmp_objects = self.sort_objects_by_draw_y()
        if tmp_objects:
            self.draw_objects(tmp_objects)

        self.coinMatrix.draw(self.game_display, self.grid_size)

        # Snowing
        self.snow.update(self.width, self.height)
        self.snow.show(self.game_display)

        # Save and load the game
        if self.game_state == 'Save':
            self.save_json()
        elif self.game_state == 'Load':
            self.load_json()
            self.coinMatrix.updateMatrix(self.road_matrix)
        pygame.display.update()  # Update of the screen
        self.clock.tick(60)

    def fill_winter(self):
        """
        Initial playground is fulfilled by winter tiles
        :return:
        """
        self.winter_tiles = []
        winter_tile_img = pygame.image.load("winter_tile_set\PNG\land\land_1.png")
        width, height = self.game_display.get_size()
        for i in range(width//winter_tile_img.get_width()):  # number of rows
            for j in range(height//winter_tile_img.get_height()):  # number of columns
                winter_tile = LandTile(i*winter_tile_img.get_width(),j*winter_tile_img.get_height(), 1)
                self.winter_tiles.append(winter_tile)

    def save_json(self):
        """
        Saves objects to JSON file with the name "my_tiles.json"
        :return:
        """
        file_name = 'my_tiles.json'

        json_structure = []

        for i in range(len(self.road_matrix.matrix)):
            for j in range(len(self.road_matrix.matrix[0])):
                if self.road_matrix.matrix[i][j] is not None:
                    road_tile = self.road_matrix.matrix[i][j]
                    road_dict = {'x': road_tile.x, 'y': road_tile.y, 'img_file_name': road_tile.img_file_name,
                                 'type': road_tile.type}
                    json_structure.append(road_dict)
                if self.build_matrix.matrix[i][j] is not None:
                    build_tile = self.build_matrix.matrix[i][j]
                    build_dict = {'x': build_tile.x, 'y': build_tile.y, 'img_file_name': build_tile.img_file_name,
                                  'type': build_tile.type}
                    json_structure.append(build_dict)
                if self.decor_matrix.matrix[i][j] is not None:
                    decor_tile = self.decor_matrix.matrix[i][j]
                    decor_dict = {'x': decor_tile.x, 'y': decor_tile.y, 'img_file_name': decor_tile.img_file_name,
                                  'type': decor_tile.type}
                    json_structure.append(decor_dict)

        with open(file_name, 'w') as outfile:
            json.dump(json_structure, outfile)

    def load_json(self):
        """
        Load the objects from the JSON file with the name "my_tiles.json"
        :return:
        """

        self.tiles = []
        with open('templates/my_tiles_1.json') as f:
            records = json.load(f)

        for record in records:
            if record['type'] == 'road':
                self.road_matrix.add(RoadTile(record['x'], record['y'], record['img_file_name']))
            elif record['type'] == 'building':
                self.build_matrix.add(Building(record['x'], record['y'], record['img_file_name']))
            else:
                self.decor_matrix.add(Decor(record['x'], record['y'], record['img_file_name']))
        print('done')












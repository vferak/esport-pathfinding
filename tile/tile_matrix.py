__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"


class TileMatrix:
    """
    Matrix of tiles. We will create a special tile matrix for road tiles, building tiles  and decoration tiles
    """
    def __init__(self, display_width, display_height, road_tile_width, road_tile_height):
        self.road_width = road_tile_width
        self.road_height = road_tile_height
        self.display_width = display_width
        self.display_height = display_height
        self.n_rows = display_width // road_tile_width
        self.n_cols = display_height // road_tile_height
        self.matrix = self.create_empty_matrix()

    def create_empty_matrix(self):
        """
        Generates an empty matrix
        :return: empty matrix
        """
        matrix = []
        for i in range(self.n_rows):
            row = []
            for j in range(self.n_cols):
                row.append(None)
            matrix.append(row)
        return matrix

    def add(self, item):
        """
        Appends a new tile to the matrix
        :param item: item
        :return:
        """
        if item.x is not None and item.y is not None:
            x_b = item.x//self.road_width
            y_b = item.y//self.road_height

            x_n = item.img.get_width()//self.road_width
            y_n = item.img.get_height()//self.road_height

            if x_n < 1:
                x_n = 1
            if y_n < 1:
                y_n = 1

            for i in range(x_n):
                for j in range(y_n):
                    self.matrix[x_b+i][y_b+j]=item

    def position_occupied(self, x, y):
        """
        Returns True and object if a position is occupied, False and None otherwise
        :param x: x-coordinate
        :param y: y-coodinate
        :return:
        """

        tmp_x = x // self.road_width
        tmp_y = y // self.road_height

        if self.matrix[tmp_x][tmp_y] is not None:
            return True, self.matrix[tmp_x][tmp_y]
        else:
            return False, None

    def del_item(self, item):
        """
        Removes a tile item from the matrix
        :param item: tile item
        :return:
        """
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.matrix[i][j] == item:
                    self.matrix[i][j] = None

    def show(self, game_display):
        """
        Show a tile set based on the matrix
        :param game_display: pygame.game_display
        :return:
        """

        shown = []

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.matrix[i][j] is not None and not self.matrix[i][j] in shown:
                    self.matrix[i][j].show(game_display)
                    shown.append(self.matrix[i][j])
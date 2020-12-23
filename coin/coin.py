import random

from myObject import MyObject


class Coin(MyObject):
    def __init__(self, roadMatrix):
        result = self.spawn(roadMatrix)
        super().__init__(result['tile'].x, result['tile'].y)

        self.column = result['column']
        self.row = result['row']

    def getAnimation(self):
        return self.getAnimationImages('coin/animation/', 9, 4, 1)

    def spawn(self, roadMatrix):
        tile = None
        row = 0
        column = 0
        while tile is None or tile.img_file_name != 'road_5.png':
            column = random.randint(0, 29)
            row = random.randint(0, 52)

            tile = roadMatrix.matrix[row][column]

        return {'tile': tile, 'column': column, 'row': row}

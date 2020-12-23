import pygame


class CoinMatrix:
    def __init__(self):
        self.coins = []
        self.matrix = []

        self.numberMatrix = []

    def updateCoins(self, coins):
        self.coins = coins
        self.__update()

    def updateMatrix(self, matrix):
        self.matrix = matrix
        self.__update()

    def __update(self):

        if self.matrix != [] and self.coins != []:
            self.numberMatrix.clear()
            for y in range(0, self.matrix.n_rows + 1):
                column = []
                for x in range(0, self.matrix.n_cols + 1):
                    column.append(None)
                self.numberMatrix.append(column)

            current = 0
            for coin in self.coins:
                self.numberMatrix[coin.row][coin.column] = current
                self.numberMatrix[coin.row][coin.column + 1] = current
                self.numberMatrix[coin.row + 1][coin.column] = current
                self.numberMatrix[coin.row + 1][coin.column + 1] = current

            while not self.isMatrixFull():
                current += 10
                for y in range(0, self.matrix.n_cols + 1):
                    for x in range(0, self.matrix.n_rows + 1):
                        if self.numberMatrix[x][y] is not None and self.numberMatrix[x][y] == current - 10:
                            if y - 1 >= 0 and self.numberMatrix[x][y - 1] is None:
                                self.numberMatrix[x][y - 1] = current
                            if y + 1 <= self.matrix.n_cols and self.numberMatrix[x][y + 1] is None:
                                self.numberMatrix[x][y + 1] = current
                            if x - 1 >= 0 and self.numberMatrix[x - 1][y] is None:
                                self.numberMatrix[x - 1][y] = current
                            if x + 1 <= self.matrix.n_rows and self.numberMatrix[x + 1][y] is None:
                                self.numberMatrix[x + 1][y] = current

    def isMatrixFull(self):
        for y in range(0, self.matrix.n_cols + 1):
            for x in range(0, self.matrix.n_rows + 1):
                if self.numberMatrix[x][y] is None:
                    return False
        return True

    def draw(self, game_display, gridSize):
        if self.matrix != [] and self.coins != []:
            myfont = pygame.font.SysFont('Comic Sans MS', 12)

            for y in range(0, self.matrix.n_cols):
                for x in range(0, self.matrix.n_rows):
                    textsurface = myfont.render(str(self.numberMatrix[x][y]), False, (0, 0, 0))
                    game_display.blit(textsurface, (x * gridSize - 1, y * gridSize - 8))

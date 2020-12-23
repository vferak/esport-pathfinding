import pygame

from tile.tile import Tile


class MyObject(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.index = 0
        self.animation = self.getAnimation()

        self.images = self.animation
        self.img = self.images[0]

    def getAnimation(self):
        return []

    def getAnimationImages(self, name, frames, zerofill=3, start=0, format='.png'):
        images = []
        for i in range(start, frames):
            img = pygame.image.load(name + str(i).zfill(zerofill) + format)
            images.append(img)

        return images

    def show(self, game_display):
        self.index = 0 if self.index >= len(self.images) - 1 else self.index + 1
        self.img = self.images[self.index]
        super().show(game_display)

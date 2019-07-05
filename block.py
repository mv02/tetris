import random
import colors

shapes = ["T", "L", "J", "S", "Z", "I", "O"]


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = []

        shape = shapes[random.randint(0, len(shapes) - 1)]

        if shape == "T":
            var1 = [(0, -1), (-1, 0), (0, 0), (1, 0)]
            var2 = [(0, -1), (0, 0), (1, 0), (0, 1)]
            var3 = [(-1, 0), (0, 0), (1, 0), (0, 1)]
            var4 = [(0, -1), (-1, 0), (0, 0), (0, 1)]
            self.tile_positions = [var1, var2, var3, var4]
            self.color = colors.PURPLE
        elif shape == "L":
            var1 = [(1, -1), (-1, 0), (0, 0), (1, 0)]
            var2 = [(0, -1), (0, 0), (0, 1), (1, 1)]
            var3 = [(-1, 0), (0, 0), (1, 0), (-1, 1)]
            var4 = [(-1, -1), (0, -1), (0, 0), (0, 1)]
            self.tile_positions = [var1, var2, var3, var4]
            self.color = colors.ORANGE
        elif shape == "J":
            var1 = [(-1, -1), (-1, 0), (0, 0), (1, 0)]
            var2 = [(0, -1), (1, -1), (0, 0), (0, 1)]
            var3 = [(-1, 0), (0, 0), (1, 0), (1, 1)]
            var4 = [(0, -1), (0, 0), (-1, 1), (0, 1)]
            self.tile_positions = [var1, var2, var3, var4]
            self.color = colors.BLUE
        elif shape == "S":
            var1 = [(0, -1), (1, -1), (-1, 0), (0, 0)]
            var2 = [(0, -1), (0, 0), (1, 0), (1, 1)]
            self.tile_positions = [var1, var2]
            self.color = colors.GREEN
        elif shape == "Z":
            var1 = [(-1, -1), (0, -1), (0, 0), (1, 0)]
            var2 = [(1, -1), (0, 0), (1, 0), (0, 1)]
            self.tile_positions = [var1, var2]
            self.color = colors.RED
        elif shape == "I":
            var1 = [(-1, 0), (0, 0), (1, 0), (2, 0)]
            var2 = [(0, -1), (0, 0), (0, 1), (0, 2)]
            self.tile_positions = [var1, var2]
            # ma byt svetle modre
            self.color = colors.PINK
        elif shape == "O":
            var1 = [(0, 0), (1, 0), (0, 1), (1, 1)]
            self.tile_positions = [var1]
            self.color = colors.YELLOW

        self.orientation = random.randint(0, len(self.tile_positions) - 1)

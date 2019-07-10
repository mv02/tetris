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
            # self.color = colors.PURPLE
            self.color = "magenta"
        elif shape == "L":
            var1 = [(1, -1), (-1, 0), (0, 0), (1, 0)]
            var2 = [(0, -1), (0, 0), (0, 1), (1, 1)]
            var3 = [(-1, 0), (0, 0), (1, 0), (-1, 1)]
            var4 = [(-1, -1), (0, -1), (0, 0), (0, 1)]
            self.tile_positions = [var1, var2, var3, var4]
            # self.color = colors.ORANGE
            self.color = "orange"
        elif shape == "J":
            var1 = [(-1, -1), (-1, 0), (0, 0), (1, 0)]
            var2 = [(0, -1), (1, -1), (0, 0), (0, 1)]
            var3 = [(-1, 0), (0, 0), (1, 0), (1, 1)]
            var4 = [(0, -1), (0, 0), (-1, 1), (0, 1)]
            self.tile_positions = [var1, var2, var3, var4]
            # self.color = colors.BLUE
            self.color = "blue"
        elif shape == "S":
            var1 = [(0, -1), (1, -1), (-1, 0), (0, 0)]
            var2 = [(0, -1), (0, 0), (1, 0), (1, 1)]
            self.tile_positions = [var1, var2]
            # self.color = colors.GREEN
            self.color = "green"
        elif shape == "Z":
            var1 = [(-1, -1), (0, -1), (0, 0), (1, 0)]
            var2 = [(1, -1), (0, 0), (1, 0), (0, 1)]
            self.tile_positions = [var1, var2]
            # self.color = colors.RED
            self.color = "red"
        elif shape == "I":
            var1 = [(-1, 0), (0, 0), (1, 0), (2, 0)]
            var2 = [(0, -1), (0, 0), (0, 1), (0, 2)]
            self.tile_positions = [var1, var2]
            # ma byt svetle modre
            # self.color = colors.PINK
            self.color = "cyan"
        elif shape == "O":
            var1 = [(0, 0), (1, 0), (0, 1), (1, 1)]
            self.tile_positions = [var1]
            # self.color = colors.YELLOW
            self.color = "yellow"

        self.orientation = random.randint(0, len(self.tile_positions) - 1)

        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        for tile_pos in self.tile_positions[self.orientation]:
            x = tile_pos[0]
            y = tile_pos[1]
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y

        self.min_x = min_x
        self.min_y = min_y

        self.width = max_x - min_x + 1
        self.height = max_y - min_y + 1

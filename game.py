import graphics
import colors
from block import Block


class Game:
    field = []
    level = 0
    score = 0
    lines = 0

    def __init__(self, field_width, field_height):
        self.field_width = field_width
        self.field_height = field_height

        for y in range(self.field_height):
            self.field.append(self.empty_row())

        self.block = None
        self.new_block()

    def new_block(self):
        del self.block
        self.block = Block(3, 0)
        self.set_tiles()
        print("LEVEL:", self.level)
        print("LINES:", self.lines)
        print("SCORE:", self.score)

    def fall(self):
        for tile in self.block.tiles:
            if not self.can_move(tile, (0, 1)):
                # dopad na zem
                for tile in self.block.tiles:
                    x = tile[0]
                    y = tile[1]
                    if y < 0:
                        return "lose"
                    self.field[y][x] = self.block.color
                cleared_lines = self.check_rows()
                if cleared_lines != 0:
                    self.check_level()
                    self.change_score(cleared_lines)
                self.new_block()
                return "ground"
        self.block.y += 1
        self.set_tiles()

    def move(self, dir):
        for tile in self.block.tiles:
            if not self.can_move(tile, (dir, 0)):
                print("Nejde posunout")
                return
        self.block.x += dir
        self.set_tiles()

    def rotate(self):
        prev_orientation = self.block.orientation
        self.block.orientation += 1
        if self.block.orientation >= len(self.block.tile_positions):
            self.block.orientation = 0
        for tile_pos in self.block.tile_positions[self.block.orientation]:
            tile = (self.block.x + tile_pos[0], self.block.y + tile_pos[1])
            if not self.free_tile(tile):
                self.block.orientation = prev_orientation
                print("Nejde otočit")
                return
        self.set_tiles()

    def set_tiles(self):
        new_tiles = []
        for tile_pos in self.block.tile_positions[self.block.orientation]:
            tile = (self.block.x + tile_pos[0], self.block.y + tile_pos[1])
            new_tiles.append(tile)
        self.block.tiles = new_tiles

    def check_rows(self):
        full_rows = []

        for y in range(self.field_height):
            full_row = True
            for x in range(self.field_width):
                tile = (x, y)
                if self.free_tile(tile):
                    full_row = False
                    break
            if full_row:
                full_rows.append(y)

        for index in full_rows:
            self.field.pop(index)
            self.field.insert(0, self.empty_row())
        cleared_lines = len(full_rows)
        self.lines += cleared_lines
        return cleared_lines

    def change_score(self, cleared):
        if cleared == 1:
            self.score += 40 * (self.level + 1)
        elif cleared == 2:
            self.score += 100 * (self.level + 1)
        elif cleared == 3:
            self.score += 300 * (self.level + 1)
        elif cleared == 4:
            self.score += 1200 * (self.level + 1)

    def check_level(self):
        if self.lines > 0 and self.lines % 5 == 0:
            self.level += 1

    def can_move(self, pos, dir):
        x = pos[0]
        y = pos[1]
        return self.free_tile((x + dir[0], y + dir[1]))

    def free_tile(self, tile):
        x = tile[0]
        y = tile[1]
        return 0 <= x < self.field_width and y < self.field_height and self.field[y][x] == colors.GAMEBG

    def empty_row(self):
        row = []
        for x in range(self.field_width):
            row.append(colors.GAMEBG)
        return row

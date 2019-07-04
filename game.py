import graphics
import colors
from block import Block


class Game:
    field = []

    def __init__(self, field_width, field_height):
        self.field_width = field_width
        self.field_height = field_height

        for y in range(self.field_height):
            self.field.append(self.empty_row())

        self.block = None
        self.new_block()

    # def start(self):
        # field[1][1] = field[1][2] = field[1][3] = field[2][2] = graphics.GREEN
        # field[1][5] = field[2][5] = field[3][5] = field[3][6] = graphics.BLUE
        # field[1][7] = field[1][8] = field[2][8] = field[3][8] = graphics.YELLOW
        # field[4][1] = field[4][2] = field[5][2] = field[5][3] = graphics.ORANGE
        # field[8][1] = field[8][2] = field[7][2] = field[7][3] = graphics.PINK
        # field[5][5] = field[5][6] = field[5][7] = field[5][8] = graphics.RED
        # field[7][7] = field[7][8] = field[8][7] = field[8][8] = graphics.PURPLE

    def new_block(self):
        del self.block
        self.block = Block(3, 0)
        self.set_tiles()

    def fall(self):
        for tile in self.block.tiles:
            if not self.can_move(tile, (0, 1)):
                # dopad na zem
                for tile in self.block.tiles:
                    x = tile[0]
                    y = tile[1]
                    self.field[y][x] = self.block.color
                self.check_rows()
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
        for y in range(self.field_height):
            full_row = True
            for x in range(self.field_width):
                tile = (x, y)
                if self.free_tile(tile):
                    full_row = False
                    break
            if full_row:
                self.field.pop(y)
                self.field.insert(0, self.empty_row())

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

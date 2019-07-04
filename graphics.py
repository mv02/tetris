import pygame
import colors

tile_size = 30
tile_padding = 1
border = 3
# margin = 10
margin = 20
margin_right = 350


class Graphics:

    def __init__(self, field_width, field_height):
        self.field_width = field_width
        self.field_height = field_height
        self.screen_width = margin + border + self.field_width * tile_size + border + margin_right
        self.screen_height = margin + border + self.field_height * tile_size + border + margin
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("TETRIS")

    def draw_block(self, block):
        for tile in block.tiles:
            if tile[0] >= 0 and tile[1] >= 0:
                self.draw_tile(tile[0], tile[1], block.color)
        pygame.display.flip()

    def remove_block(self, block):
        for tile in block.tiles:
            if tile[0] >= 0 and tile[1] >= 0:
                self.draw_tile(tile[0], tile[1], colors.GAMEBG)
        pygame.display.flip()

    def draw_window(self):
        self.screen.fill(colors.WINDOWBG)
        self.screen.fill(colors.BORDER, pygame.Rect(margin, margin, self.field_width * tile_size + 2 * border, self.field_height * tile_size + 2 * border))
        pygame.display.flip()

    def draw_field(self, field):
        for y in range(len(field)):
            for x in range(len(field[y])):
                self.draw_tile(x, y, field[y][x])
        pygame.display.flip()
        print("Překresleno")

    def draw_tile(self, x, y, color):
        self.draw_square(margin + border + x * tile_size, margin + border + y * tile_size, tile_size, colors.GAMEBG)
        self.draw_square(margin + border + x * tile_size + tile_padding, margin + border + y * tile_size + tile_padding, tile_size - 2 * tile_padding, color)

    def draw_square(self, x, y, size, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, size, size))

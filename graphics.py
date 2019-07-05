import pygame
import colors

tile_size = 30
tile_padding = 1
border = 3
# margin = 10
margin = 20
# margin_right = 350
info_width = 200
info_height = 100
info_padding = 10

pygame.font.init()
font1 = pygame.font.Font(None, 28)
font2 = pygame.font.Font("digital-7.ttf", 28)

class Graphics:

    def __init__(self, field_width, field_height):
        self.game_width = field_width * tile_size
        self.game_height = field_height * tile_size
        self.screen_width = margin + border + self.game_width + border + margin + border + info_width + border + margin
        self.screen_height = margin + border + self.game_height + border + margin
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("TETRIS")

        self.info_x = 2 * margin + 3 * border + self.game_width
        self.info_y1 = margin + border
        self.info_y2 = 2 * margin + 3 * border + info_height
        self.info_y3 = 3 * margin + 5 * border + 1.5 * info_height
        self.info_y4 = 4 * margin + 7 * border + 2 * info_height

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
        self.screen.fill(colors.BORDER, pygame.Rect(margin, margin, self.game_width + 2 * border, self.game_height + 2 * border))
        pygame.display.flip()

    def draw_level(self, level):
        text = font1.render("LEVEL:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y2 + info_height / 4 - text_height / 2, text_width, text_height))

        text = font2.render(str(level), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y2 + info_height / 4 - text_height / 2, text_width, text_height))

    def draw_lines(self, lines):
        text = font1.render("LINES:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y3 + info_height / 4 - text_height / 2, text_width, text_height))

        text = font2.render(str(lines), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y3 + info_height / 4 - text_height / 2, text_width, text_height))

    def draw_score(self, score):
        text = font1.render("SCORE:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y4 + info_height / 4 - text_height / 2, text_width, text_height))

        text = font2.render(str(score), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y4 + info_height / 4 - text_height / 2, text_width, text_height))

    def draw_next(self, block):
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y1 - border, 2 * border + info_width, 2 * border + info_height))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y1, info_width, info_height))
        for tile in block.tiles:
            self.draw_square(self.info_x + info_width / 2 - tile_size / 2 + tile[0], self.info_y1 + info_height / 2 - tile_size / 2 + tile[1], tile_size, block.color)
            # self.draw_square(350, 50, tile_size, block.color)
        pygame.display.flip()

    def draw_info(self, level, lines, score):
        # level
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y2 - border, 2 * border + info_width, 2 * border + info_height / 2))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y2, info_width, info_height / 2))
        # lines
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y3 - border, 2 * border + info_width, 2 * border + info_height / 2))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y3, info_width, info_height / 2))
        # score
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y4 - border, 2 * border + info_width, 2 * border + info_height / 2))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y4, info_width, info_height / 2))

        self.draw_level(level)
        self.draw_lines(lines)
        self.draw_score(score)
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

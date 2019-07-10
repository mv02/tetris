import pygame
import random
import colors

tile_size = 30
tile_padding = 1
border = 3
# margin = 10
margin = 20
info_width = 200
info_height = 200
info_padding = 10

pygame.font.init()
font1 = pygame.font.Font(None, 28)
font2 = pygame.font.Font("digital-7.ttf", 28)
font3 = pygame.font.Font("digital-7.ttf", 60)


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
        self.info_y3 = 3 * margin + 5 * border + 1.25 * info_height
        self.info_y4 = 4 * margin + 7 * border + 1.5 * info_height

    def draw_block(self, block):
        for tile in block.tiles:
            if tile[0] >= 0 and tile[1] >= 0:
                self.draw_tile(self.screen, tile[0], tile[1], block.color, margin, border)
        pygame.display.flip()

    def remove_block(self, block):
        for tile in block.tiles:
            if tile[0] >= 0 and tile[1] >= 0:
                self.draw_tile(self.screen, tile[0], tile[1], colors.GAMEBG, margin, border)
        pygame.display.flip()

    def draw_window(self):
        self.screen.fill(colors.WINDOWBG)
        self.screen.fill(colors.BORDER, pygame.Rect(margin, margin, self.game_width + 2 * border, self.game_height + 2 * border))
        pygame.display.flip()

    def draw_level(self, level):
        text = font1.render("LEVEL:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y2 + info_height / 8 - text_height / 2, text_width, text_height))

        text = font2.render(str(level), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y2 + info_height / 8 - text_height / 2, text_width, text_height))

    def draw_lines(self, lines):
        text = font1.render("LINES:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y3 + info_height / 8 - text_height / 2, text_width, text_height))

        text = font2.render(str(lines), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y3 + info_height / 8 - text_height / 2, text_width, text_height))

    def draw_score(self, score):
        text = font1.render("SCORE:", True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_padding, self.info_y4 + info_height / 8 - text_height / 2, text_width, text_height))

        text = font2.render(str(score), True, colors.BORDER)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.blit(text, pygame.Rect(self.info_x + info_width - info_padding - text_width, self.info_y4 + info_height / 8 - text_height / 2, text_width, text_height))

    def draw_next(self, block):
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y1 - border, 2 * border + info_width, 2 * border + info_height))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y1, info_width, info_height))

        surf_width = block.width * tile_size
        surf_height = block.height * tile_size
        surf = pygame.Surface((surf_width, surf_height))
        surf.fill(colors.GAMEBG)
        for tile_pos in block.tile_positions[block.orientation]:
            x = abs(block.min_x) + tile_pos[0]
            y = abs(block.min_y) + tile_pos[1]
            self.draw_tile(surf, x, y, block.color, 0, 0)
        self.screen.blit(surf, pygame.Rect(self.info_x + info_width / 2 - surf_width / 2, self.info_y1 + info_height / 2 - surf_height / 2, block.width * tile_size, block.height * tile_size))
        pygame.display.flip()

    def draw_info(self, level, lines, score):
        # level
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y2 - border, 2 * border + info_width, 2 * border + info_height / 4))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y2, info_width, info_height / 4))
        # lines
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y3 - border, 2 * border + info_width, 2 * border + info_height / 4))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y3, info_width, info_height / 4))
        # score
        self.screen.fill(colors.BORDER, pygame.Rect(self.info_x - border, self.info_y4 - border, 2 * border + info_width, 2 * border + info_height / 4))
        self.screen.fill(colors.GAMEBG, pygame.Rect(self.info_x, self.info_y4, info_width, info_height / 4))

        self.draw_level(level)
        self.draw_lines(lines)
        self.draw_score(score)
        pygame.display.flip()

    def draw_field(self, field):
        for y in range(len(field)):
            for x in range(len(field[y])):
                self.draw_tile(self.screen, x, y, field[y][x], margin, border)
        pygame.display.flip()
        # print("Překresleno")

    def draw_tile(self, surf, x, y, color, margin, border):
        self.draw_square(surf, margin + border + x * tile_size, margin + border + y * tile_size, tile_size, colors.GAMEBG)
        # self.draw_square(surf, margin + border + x * tile_size + tile_padding, margin + border + y * tile_size + tile_padding, tile_size - 2 * tile_padding, color)
        if color != colors.GAMEBG:
            self.draw_image(surf, margin + border + x * tile_size + tile_padding, margin + border + y * tile_size + tile_padding, tile_size - 2 * tile_padding, color)

    def draw_square(self, surf, x, y, size, color):
        pygame.draw.rect(surf, color, pygame.Rect(x, y, size, size))

    def draw_image(self, surf, x, y, size, color):
        image = pygame.image.load("textures\\" + color + ".png")
        image = pygame.transform.scale(image, (size, size))
        surf.blit(image, pygame.Rect(x, y, size, size))

    def game_over(self):
        text = font3.render("GAME OVER", True, colors.RED)
        text_width = text.get_width()
        text_height = text.get_height()
        self.screen.fill(colors.BLACK)
        self.screen.blit(text, pygame.Rect(self.screen_width / 2 - text_width / 2, self.screen_height / 2 - text_height / 2, text_width, text_height))
        pygame.display.flip()

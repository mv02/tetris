import pygame
from graphics import Graphics
from game import Game
from block import Block

pygame.init()

game = Game(10, 20)
graphics = Graphics(10, 20)

graphics.draw_window()
graphics.draw_info(game.level, game.lines, game.score)
graphics.draw_field(game.field)

drop_event = pygame.USEREVENT + 1
pygame.time.set_timer(drop_event, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_r:
                graphics.remove_block(game.block)
                game.rotate()
                graphics.draw_block(game.block)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                graphics.remove_block(game.block)
                game.move(1)
                graphics.draw_block(game.block)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                graphics.remove_block(game.block)
                game.move(-1)
                graphics.draw_block(game.block)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pygame.time.set_timer(drop_event, 40)
        elif event.type == drop_event:
            graphics.remove_block(game.block)
            state = game.fall()
            if state == "ground":
                graphics.draw_field(game.field)
                pygame.time.set_timer(drop_event, 300)
            elif state == "score":
                graphics.draw_field(game.field)
                graphics.draw_info(game.level, game.lines, game.score)
                pygame.time.set_timer(drop_event, 300)
            elif state == "lose":
                pygame.quit()
            graphics.draw_block(game.block)

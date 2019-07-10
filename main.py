import pygame
import sys
from graphics import Graphics
from game import Game
from block import Block

pygame.init()

game = Game(10, 20)
graphics = Graphics(10, 20)

graphics.draw_window()
graphics.draw_info(game.level, game.lines, game.score)
graphics.draw_field(game.field)

game.new_block(Block(4, 0))
next_block = Block(4, 0)
graphics.draw_next(next_block)

speed = 300
drop_event = pygame.USEREVENT + 1
pygame.time.set_timer(drop_event, speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_p:
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                paused = False
                                break
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
                game.new_block(next_block)
                next_block = Block(4, 0)
                graphics.draw_next(next_block)
                pygame.time.set_timer(drop_event, speed)
            elif "score" in state:
                graphics.draw_field(game.field)
                graphics.draw_info(game.level, game.lines, game.score)
                game.new_block(next_block)
                next_block = Block(4, 0)
                graphics.draw_next(next_block)

                level = state.replace("score", "")
                if speed > 60:
                    speed = 300 - int(level) * 5
                pygame.time.set_timer(drop_event, speed)
            elif state == "lose":
                graphics.game_over()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()
            graphics.draw_block(game.block)
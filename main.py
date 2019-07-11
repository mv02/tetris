import pygame
import os.path
from graphics import Graphics
from game import Game
from block import Block
import save
import load


def quit():
    pygame.quit()
    exit()


def quit_save():
    save.save(game.field, game.level, game.lines, game.score, game.block, next_block)
    quit()


def quit_del_save():
    if os.path.exists("save.xml"):
        os.remove("save.xml")
    quit()


def new_block():
    global next_block
    game.set_block(next_block)
    next_block = Block(4, 0, None, None)


pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

game = Game(10, 20)
graphics = Graphics(10, 20)

if os.path.exists("save.xml"):
    chosen = 1
    graphics.menu(chosen)
    choice = 0

    while choice == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if chosen > 1:
                        chosen -= 1
                    graphics.menu(chosen)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if chosen < 3:
                        chosen += 1
                    graphics.menu(chosen)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    choice = chosen
    if choice == 1:
        savegame = load.load()
        game.level = int(savegame[0])
        game.lines = int(savegame[1])
        game.score = int(savegame[2])
        game.set_block(Block(4, 0, savegame[3][0], int(savegame[3][1])))
        next_block = Block(4, 0, savegame[4][0], int(savegame[4][1]))
        game.field = savegame[5]
    elif choice == 2:
        next_block = Block(4, 0, None, None)
        new_block()
    elif choice == 3:
        quit()
else:
    next_block = Block(4, 0, None, None)
    new_block()

graphics.draw_window()
graphics.draw_info(game.level, game.lines, game.score)
graphics.draw_field(game.field)
graphics.draw_next(next_block)

speed = 300 - game.level * 10
if speed < game.max_speed:
    speed = game.max_speed
drop_event = pygame.USEREVENT + 1
pygame.time.set_timer(drop_event, speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_save()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_save()
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
                new_block()
                pygame.time.set_timer(drop_event, speed)
            elif state == "score":
                graphics.draw_field(game.field)
                new_block()
                graphics.draw_info(game.level, game.lines, game.score)
                speed = 300 - game.level * 10
                if speed < game.max_speed:
                    speed = game.max_speed
                pygame.time.set_timer(drop_event, speed)
            elif state == "lose":
                graphics.game_over()
                pygame.time.delay(2000)
                quit_del_save()
            graphics.draw_block(game.block)
            graphics.draw_next(next_block)
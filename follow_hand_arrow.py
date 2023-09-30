import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

moving = True

is_arrive = True

xPos, yPos = TUK_WIDTH // 2, TUK_HEIGHT // 2

frame = 0

HandPos = [random.randint(100, TUK_WIDTH - 100), random.randint(100, TUK_HEIGHT - 100)]

prevframe = False

def handle_events():

    global moving

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            moving = False

while moving:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if abs(HandPos[0] - xPos) < 1 and abs(HandPos[1] == yPos) < 1:
        is_arrive = True
    if is_arrive:
        HandPos = [random.randint(100, TUK_WIDTH - 100), random.randint(100, TUK_HEIGHT - 100)]
        is_arrive = False
    hand_arrow.draw(HandPos[0], HandPos[1])
    if HandPos[0] > xPos:
        if prevframe:
            prevframe = False
            frame = 0
        character.clip_draw(frame % 8 * 100, 100, 100, 100, xPos, yPos)

    else:
        if not prevframe:
            prevframe = True
            frame = 0
        character.clip_draw(frame % 8 * 100, 0, 100, 100, xPos, yPos)

    t = 0.13

    xPos = (1-t) * xPos + t * HandPos[0]
    yPos = (1-t) * yPos + t * HandPos[1]

    frame += 1

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

moving = True
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
    # character.clip_draw()

    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()
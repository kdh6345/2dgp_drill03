#2022184001
from pico2d import *
import random
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
    clear_canvas_now()
    character.draw_now(400,300)
    delay(1)
    pass
def run_circle():
    print('CIRCLE')
    
    clear_canvas_now()
    character.draw_now(400,300)
    delay(1)
    pass


while True:
    run_rectangle()
    run_circle()
    break
    
close_canvas()

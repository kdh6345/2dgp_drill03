#2022184001
from pico2d import *
import random
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
def run_top():
    pass
def run_bottom():
    pass
def run_right():
    pass
def run_left():
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    clear_canvas_now()
    character.draw_now(400,300)
    delay(1)
    pass

def run_circle():
    print('CIRCLE')
    
    r,cx,cy=300,800//2,600//2
   
    for d in range(0,360):
        x=r*math.cos(math.radians(d))+cx
        y=r*math.sin(math.radians(d))+cy
    
        clear_canvas_now()
        character.draw_now(x,y)
        delay(0.01)
    pass


while True:
    run_rectangle()
    run_circle()
    break
    
close_canvas()

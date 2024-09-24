#2022184001
from pico2d import *
import random
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.01)
    
def run_top():
    print('top')
    for x in range(20,750,10):
        draw_boy(x,550)
    pass
def run_bottom():
    print('bottom')
    for x in range(750,20,-10):
        draw_boy(x,50)
    pass
def run_right():
    print('right')
    for y in range(550,0,-10):
        draw_boy(750,y)
    pass
def run_left():
    print('left')
    for y in range(0,550,10):
        draw_boy(0,y)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    
    pass

def run_circle():
    print('CIRCLE')
    
    r,cx,cy=300,800//2,600//2
   
    for d in range(0,360):
        x=r*math.cos(math.radians(d))+cx
        y=r*math.sin(math.radians(d))+cy
    
        draw_boy(x,y)
    pass


while True:
    #run_circle()
    run_rectangle()
    break
    
close_canvas()

#2022184001 Drill3
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
    for x in range(50,750,10):
        draw_boy(x,550)
    pass
def run_bottom():
    print('bottom')
    for x in range(750,50,-10):
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
        draw_boy(50,y)
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

def run_t1():
    print('T1')
    for x in range(50,750,10):
        draw_boy(x,50)
    pass
def run_t2():
    print('T2')
    x, y = 750, 50
    while x > 400:
        x -= math.cos(math.radians(45)) * 10  
        y += math.sin(math.radians(45)) * 10
        draw_boy(x, y)
    pass

    
def run_t3():
    print('T3')
    x, y = 400, 400
    while x > 50:
        x -= math.cos(math.radians(45)) * 10  
        y -= math.sin(math.radians(45)) * 10  
        draw_boy(x, y)
    pass

def run_triangle():
    print('TRIANGLE')
    run_t1()
    run_t2()
    run_t3()
    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()
    
close_canvas()

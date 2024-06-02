from collections import deque
import pygame as pg
from Elevator import Elevator
from Floor import Floor
from Architect import Building
call = 0

# class manager:
    
    # def __init__(self) -> None:
        # self.order = 1
        
def call(mouse_position,num_floors, building,screen):
        x1, y1 = mouse_position
        for floor in building.floors:
            x2, y2 = floor.button
            if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2:
                floor.drew_button(screen,floor.roof_position,call)
                pg.display.flip()
                return floor.number
            
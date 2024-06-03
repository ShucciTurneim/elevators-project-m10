from collections import deque
import pygame as pg
from Elevator import Elevator
from Floor import Floor
from Architect import Building
from elevator_selection import elevator_selection
call = 0
stand_by = 2
screen_color =(255,255,255)

def travels(screen,priority_elevator, dst):
        stop = dst.roof_position
        location = priority_elevator.current_location
        right_side = priority_elevator.position + priority_elevator.width
        while location != stop:
            rect = pg.Rect(priority_elevator.position, location, priority_elevator.width, priority_elevator.height)
            if location < stop:
                screen.fill(screen_color,rect)
                location += 1
                screen.blit(priority_elevator.IMAGE, (priority_elevator.position, location))   
            elif location > stop:
                screen.fill(screen_color, rect)
                location -= 1
                screen.blit(priority_elevator.IMAGE, (priority_elevator.position, location))    
            pg.display.flip() 
            pg.time.Clock().tick(60)  
        priority_elevator.current_location = stop 
        
def call(mouse_position,num_floors, building, screen):
    x1, y1 = mouse_position
    for floor in building.floors:
        x2, y2 = floor.button
        if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2:
            floor.drew_button(screen,floor.roof_position,call)
            pg.display.flip()
            priority_elevator, time_left = elevator_selection(floor.number,building)
            priority_elevator.send_order(floor.number, building, screen)
            floor.show_arrival_time(screen, time_left)
            travels(screen,priority_elevator, floor)
            priority_elevator.finish_order()
                
            

            
from collections import deque
import pygame as pg
from Elevator import Elevator
from Floor import Floor
from Architect import Building
from elevator_selection import elevator_selection
import time

call = 0
stand_by = 2
screen_color =(255,255,255)
black_space_color = (0, 0, 0)
numbers_default_color = (225, 0, 0)
numbers_on_hold_color = (255,215,0)
button_default_color = (128, 128, 128)
button_on_hold_color = (0, 128, 0 ,128)
height_img = 57
width_img = 64
black_space_thickness  = 7
height = height_img + black_space_thickness
width = width_img
timer_width = 64
builder = order_completed = 1

def show_arrival_time(screen,building):
    for floor in building.floors:
        print(floor,floor.made_order)
        if floor.made_order:
            font = pg.font.Font(None, int(height_img/2)) 
            if floor.time_left != 0.0:
                pg.draw.rect(screen, black_space_color, floor.timer_Rect)
                number = font.render(f'{floor.time_left}', True, button_on_hold_color)
                screen.blit(number, floor.clock_position)
                pg.display.flip()    
                floor.floor_timer = floor.time_left    
                floor.time_left -= 0.5
            else: 
                floor.drew_button(screen, floor.roof_position, order_completed)                   
    # time.sleep(0.5)        
    
def update_finish(building):
    for elevator in building.elevators:
        if not elevator.travels:
            if len(elevator.que) > 0:  
                elevator.finish_order(building)    
            



def travels(screen,building):
    
    for elevator in building.elevators:                                     #
        # print(elevator.number,elevator.travels)
        if elevator.travels:
            dest_y = building.floors[elevator.dst].roof_position
            if elevator.current_location < dest_y:         #dst= roof_position  #                
                elevator.current_location += 5
                building.update_elevators(screen)   
            elif elevator.current_location > dest_y:
                elevator.current_location -= 5
                building.update_elevators(screen)   
            else: 
                elevator.travels = False
                   
            #location = priority_elevator.current_location    
            pg.display.flip() 
            pg.time.Clock().tick(60)
        #priority_elevator.current_location = stop 
        
def call(building,event,screen):
    left = 1
    if event.type == pg.MOUSEBUTTONDOWN and event.button  == left:
        print(event)
        mouse_position = pg.mouse.get_pos() 
        x1, y1 = mouse_position
        for floor in building.floors:
            x2, y2 = floor.button
            if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2:
                if not floor.made_order:
                    floor.made_order = True
                    floor.drew_button(screen,floor.roof_position,call)
                    pg.display.flip()
                    priority_elevator, floor.time_left = elevator_selection(floor.number,building)
                    priority_elevator.send_order(floor.number, building, screen)
                    # show_arrival_time(screen, building)
           

                
            

            
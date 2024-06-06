from collections import deque
import pygame as pg
from Elevator import Elevator
from Floor import Floor
from Architect import Building
from elevator_selection import elevator_selection
import time
import threading

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
builder = order_completed = -1

def show_arrival_time(screen,building):
    for floor in building.floors:
        if floor.made_order and floor.time_on:
                font = pg.font.Font(None, int(height_img/2)) 
                floor.drew_button(screen, floor.roof_position,stand_by )
                if floor.time_left != 0.0:
                    pg.draw.rect(screen, black_space_color, floor.timer_Rect)
                    number = font.render(f'{floor.time_left}', True, button_on_hold_color)
                    screen.blit(number, floor.clock_position)     
                    floor.time_left -= 0.5
                else: 
                    # pg.draw.rect(screen, black_space_color, floor.timer_Rect)
                    # number = font.render(f'{0.0}', True, button_on_hold_color)
                    # screen.blit(number, floor.clock_position)  
                    floor.drew_button(screen, floor.roof_position, order_completed)
                    pg.draw.rect(screen, screen_color, floor.timer_Rect)
                      
                building.update_time = time.time()                      
                floor.time_on = False
                
# def update_time():
    
                   
    
# def show_time(screen,building):
    # show_timing = threading.Thread(target=show_arrival_time,args=(screen,building))    
    # show_timing.start()
        
# def travels(screen,building):
    
#     for elevator in building.elevators:  
#         height_floor = building.floors[elevator.dst].height
#         if elevator.travels:
#             new_time = time.time()
#             half_a_second = new_time - building.update_time
#             if  half_a_second >= 0.5:
#                  for floor in elevator.que:
#                     building.floors[floor].time_on = True
#             if new_time - elevator.stop_time >= 2:
#                 dest_y = building.floors[elevator.dst].roof_position
#                 if elevator.current_location == dest_y:
#                     elevator.finish_order(building)   
#                 elif  half_a_second >= 0.5:
#                     vector = (dest_y - elevator.current_location)/abs(dest_y - elevator.current_location)
#                     while elevator.current_location / height_floor != elevator.current_location // height_floor:
#                         elevator.current_location +=  vector    
#                 else:   
#                     vector = (dest_y - elevator.current_location)/abs(dest_y - elevator.current_location)   
#                     elevator.current_location +=  vector
#                     building.update_elevators(screen)

def update_arrival_time(building,screen):
    current_time = time.time()
    for floor in building.floors:
        if floor.made_order and current_time - floor.start_clock >= 0.28:
            floor.time_left -= 0.3
            floor.time_left = int(floor.time_left*10)/10
            floor.draw_timer_display(screen,True)
            floor.start_clock = time.time()
            if 0.0 <= floor.time_left <= 0.35:
                floor.made_order = False
                floor.draw_timer_display(screen,False)
                floor.drew_button(screen, floor.roof_position,order_completed)
            

def travels(screen,building):
    for elevator in building.elevators:         
        if elevator.dst != elevator.departure and elevator.in_travel:
            dest_y = building.floors[elevator.dst].roof_position     
            if dest_y != elevator.current_location:
                vector = (dest_y - elevator.current_location)/abs(dest_y - elevator.current_location)*2  
                elevator.current_location +=  vector
                building.update_elevators(screen)
            else:
                elevator.stop_time = time.time()
                elevator.in_travel = False
                print (elevator.number,elevator.elapsed_time(building))
                
                    
                
def call(building,event,screen):
    left = 1
    if event.type == pg.MOUSEBUTTONDOWN and event.button  == left:
        mouse_position = pg.mouse.get_pos() 
        x1, y1 = mouse_position
        for floor in building.floors:
            x2, y2 = floor.button
            if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2 and not floor.made_order:
                elevator_at_floor = []
                for elevator in building.elevators: 
                    elevator_at_floor.append(elevator.current_location)
                if floor.roof_position not in elevator_at_floor:
                    print(floor.number)
                    # if not floor.made_order:
                    floor.made_order = True
                    # floor.time_on = True
                    elevator_selection(floor,building,screen)
                        
                    
           

                
            

            
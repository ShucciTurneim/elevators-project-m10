from collections import deque
import pygame as pg
from Elevator import Elevator
from Floor import Floor
from Architect import Building
from elevator_selection import elevator_selection
call = 0
stand_by = 2
screen_color =(255,255,255)

def travels(screen,building):
    
    for elevator in building.elevators:                                     #
        if elevator.travels:
            if elevator.current_location < elevator.dst:         #dst= roof_position  #                
                elevator.current_location += 1
                building.update_elevators(screen)   
            elif elevator.current_location > elevator.dst:
                print(elevator.current_location,elevator.dst) 
                elevator.current_location -= 20
                building.update_elevators(screen)   
            #location = priority_elevator.current_location    
            pg.display.flip() 
            pg.time.Clock().tick(60)
        #priority_elevator.current_location = stop 
        
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
            travels(screen,building)
            priority_elevator.finish_order()
                
            

            
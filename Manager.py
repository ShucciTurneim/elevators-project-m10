
import pygame as pg
from Elevator import Elevator
from Floor import Floor
import time
from Data_base import *

class Manager:
    def __init__(self):
        self.__elevators = []
        self.__floors = []
        
    def elevators_builder(self,elevators_num, screen):
        for num_elevator in range(elevators_num):
            elevator = Elevator(num_elevator)
            elevator.build_elevator(num_elevator,screen)
            self.__elevators.append(elevator)
        
        
    def floors_builder(self,num_floors,screen, screen_height):
            for num_floor in range(num_floors):
                floor = Floor(num_floor)
                floor.build_floor(num_floor,screen,screen_height)
                self.__floors.append(floor)


    def new_building_architect(self,floors_num, elevators_num, screen):
            screen_height = pg.display.get_surface().get_height()
            self.floors_builder(floors_num,screen, screen_height)
            self.elevators_builder(elevators_num, screen)
      
        
    def elevator_selection(self,floor,screen):
        dst = floor.number 
        min_arrival_time = float('inf')
        for elevator in self.__elevators:  
            arrival_time = elevator.arrival_time(dst)
            if min_arrival_time > arrival_time: 
                min_arrival_time = arrival_time
                priority_elevator = elevator       
        floor.request_in_process(min_arrival_time,screen)
        priority_elevator.send_order(dst)


    def call(self,event,screen):
        left = 1
        if event.type == pg.MOUSEBUTTONDOWN and event.button  == left:
            mouse_position = pg.mouse.get_pos() 
            x1, y1 = mouse_position
            for floor in self.__floors:
                x2, y2 = floor.button
                if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2 and not floor.made_order:
                    elevator_at_floor = []
                    for elevator in self.__elevators: 
                        elevator_at_floor.append(elevator.current_location)
                    if floor.roof_position not in elevator_at_floor:
                        floor.made_order = True
                        self.elevator_selection(floor,screen)


    def update_arrival_time(self,manager,screen):
        for floor in manager.__floors:           
               floor.display_clock(screen)     
                    
                        
    def travels(self,screen):
        for elevator in self.__elevators:         
            if elevator.in_travel:  
                dest = self.__floors[elevator.dst]                                            
                dest_y = dest.roof_position    
                elevator.travel(dest_y,screen)                                            
                    
                    
    def close_finish_orders(self):
        current_time = time.time()
        for elevator in self.__elevators:
            dest_y = self.__floors[elevator.dst].roof_position
            if dest_y == elevator.current_location and 2 <= current_time - elevator.stop_time < current_time:
                elevator.stop_time = 0
                elevator.finish_order()                
                    
                
                    

            
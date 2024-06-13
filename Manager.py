
import pygame as pg
from Elevator import Elevator
from Floor import Floor
import time
from Data_base import *

class Manager:
    def __init__(self,floors_number, elevators_numbers, screen):
        self.__elevators = []
        self.__floors = []
        self.elevators_builder(elevators_numbers, screen)
        self.floors_builder(floors_number,screen)
        
        
        # Creates an object and adds to the object set
    def elevators_builder(self,elevators_num, screen):
        for num_elevator in range(elevators_num):
            elevator = Elevator(num_elevator)
            elevator.build_elevator(num_elevator,screen)
            self.__elevators.append(elevator)
        
        # Creates an object and adds to the object set
    def floors_builder(self,num_floors,screen):
        screen_height = pg.display.get_surface().get_height()
        for num_floor in range(num_floors):
            floor = Floor(num_floor)
            floor.build_floor(num_floor,screen,screen_height)
            self.__floors.append(floor)
      
        #Finds the elevator with the shortest route, and updates the elevator and the floor.
    def elevator_selection(self,floor,screen):
        dst = floor.number 
        min_arrival_time = float('inf')
        for elevator in self.__elevators:  
            arrival_time = elevator.arrival_time(dst)   # # Calculates arrival time to a given destination
            if min_arrival_time > arrival_time: 
                min_arrival_time = arrival_time
                priority_elevator = elevator       
        floor.request_in_process(min_arrival_time,screen)   #updates the floor
        priority_elevator.send_order(dst)                   #updates the elevator

    # Filter mouse clicks. Receives and filters readings orders. Calling the elevator selector
    def call(self,event,screen):
        left = 1
        if event.type == pg.MOUSEBUTTONDOWN and event.button  == left:              # Filter mouse clicks
            mouse_position = pg.mouse.get_pos() 
            x1, y1 = mouse_position
            for floor in self.__floors:
                x2, y2 = floor.button
                if (x1-x2)**2 +(y1-y2)**2 <= floor.button_radius**2 and not floor.made_order:       # Pythagoras
                    elevator_at_floor = []
                    for elevator in self.__elevators: 
                        elevator_at_floor.append(elevator.current_location)
                        if floor.permission_checker(elevator_at_floor):         # Checks that there is no elevator on the floor  
                            self.elevator_selection(floor,screen)               # Calling the elevator selector


        #Updates the countdown on each iteration
    def update_arrival_time(self,manager,screen):
        for floor in manager.__floors:           
               floor.display_clock(screen)     
                    
        # Locates the target and moves the elevator in the direction       
    def travels(self,screen):
        for elevator in self.__elevators:         
            if elevator.in_travel: 
                dest = self.__floors[elevator.dst]                                     
                dest_y = dest.get_roof_position()   # Locates the target
                elevator.travel(dest_y,screen)     # moves the elevator in the direction                                         
                    
                    
    def close_finish_orders(self):
        current_time = time.time()
        for elevator in self.__elevators:
            dest = self.__floors[elevator.dst]
            dest_y = dest.get_roof_position() 
            elevator.finish_order(dest_y,current_time)                
                    
                
                    

            
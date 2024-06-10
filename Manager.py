
import pygame as pg
from Elevator import Elevator
from Floor import Floor
import time
order_completed = -1

class Manager:
    def __init__(self):
        self.__elevators = []
        self.__floors = []
        
    def elevators_builder(self,elevators_num, screen, screen_height,A):
        for num_elevator in range(elevators_num):
            elevator = Elevator(num_elevator)
            elevator.build_elevator(num_elevator, screen_height, A)
            self.set_elevators(elevator)
        self.update_elevators(screen,A)   
        
        
    def floors_builder(self,num_floors,screen, screen_height,A):
            for num_floor in range(num_floors):
                floor = Floor(num_floor)
                floor.build_floor(num_floor,screen,screen_height,A)
                self.set_floors(floor)


    def new_building_architect(self,floors_num, elevators_num, screen,A):
            screen_height = pg.display.get_surface().get_height()
            self.floors_builder(floors_num,screen, screen_height,A)
            self.elevators_builder(elevators_num, screen, screen_height, A)
      

    def get_elevators(self):
        return self.__elevators
        
    def set_elevators(self,elevator):
        self.__elevators.append(elevator)
        
    def set_floors(self,floor):
        self.__floors.append(floor)    
        
    def elevator_selection(self,floor,screen, A):
        dst = floor.number 
        min = float('inf')
        for elevator in self.__elevators:  
            dst_distance = abs(elevator.absolute_stop - dst)/2  
            arrival_time = elevator.operation_duration + dst_distance - elevator.elapsed_time()
            if min > arrival_time: 
                min = arrival_time
                priority_elevator = elevator      
        arrival_time = min  
        floor.request_in_process(arrival_time,screen, A)
        priority_elevator.send_order(dst)


    def call(self,event,screen, A):
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
                        self.elevator_selection(floor,screen, A)


    def update_arrival_time(self,manager,screen, A):
        for floor in manager.__floors:           
               floor.display_clock(screen,A)     
                    
                        
    def travels(self,screen,A):
        for elevator in self.__elevators:         
            if elevator.dst != elevator.departure and elevator.in_travel:
                dest = self.__floors[elevator.dst]                                            
                dest_y = dest.roof_position    
                elevator.travel(dest_y,screen, A, self)                                            
                
                
                        #Updates location of elevators During the construction phase and the travel phase
    def update_elevators(self, screen,A):
        for elevator in self.get_elevators():    # x,            y
            elevator.position = elevator.width_position,elevator.current_location      
            rect = pg.Rect(elevator.width_position, elevator.current_location , A.width_elevator, A.height_elevator)
            screen.fill(A.screen_color,rect)
            screen.blit(A.elevator_IMAGE, (elevator.position))
                    
                    
    def close_finish_orders(self):
        current_time = time.time()
        for elevator in self.__elevators:
            dest_y = self.__floors[elevator.dst].roof_position
            if dest_y == elevator.current_location and 2 <= current_time - elevator.stop_time < current_time:
                elevator.stop_time = 0
                elevator.finish_order()                
                    
                
                    

            
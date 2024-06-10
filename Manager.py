
import pygame as pg
import time
order_completed = -1

class Manager:
    def __init__(self):
        self.__elevators = []
        self.__floors = []

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
        current_time = time.time()
        for floor in manager.__floors:
            if floor.made_order and current_time - floor.start_clock >= 0.1:
                floor.time_left -= (current_time - floor.start_clock)
                floor.draw_timer_display(screen,True, A)
                floor.start_clock = time.time()
                if  floor.time_left <= 0.0:
                    floor.made_order = False
                    floor.draw_timer_display(screen,False, A)
                    floor.drew_button(screen, floor.roof_position,order_completed, A)             
                    
                    
    def find_direction(self,dest_y,elevator):
        return (dest_y - elevator.current_location)/abs(dest_y - elevator.current_location)                
                    
    def steps(self,dest_y,elevator):
        mov_direction = self.find_direction(dest_y,elevator)
        vector = mov_direction*2  
        elevator.current_location +=  vector                        
        if dest_y != elevator.current_location and mov_direction != self.find_direction(dest_y,elevator):
            elevator.current_location = dest_y  
                        
    def travels(self,screen,A):
        for elevator in self.__elevators:         
            if elevator.dst != elevator.departure and elevator.in_travel:
                dest = self.__floors[elevator.dst]                                            #
                dest_y = dest.roof_position     
                if dest_y != elevator.current_location:
                    self.steps(dest_y,elevator)
                    A.update_elevators(screen,self)
                else:
                    elevator.stop_time = time.time()
                    elevator.in_travel = False
                    pg.mixer.music.load(A.ding)
                    pg.mixer.music.play()
                    
                    
    def close_finish_orders(self,manager):
        current_time = time.time()
        for elevator in manager.__elevators:
            dest_y = manager.__floors[elevator.dst].roof_position
            if dest_y == elevator.current_location and 2 <= current_time - elevator.stop_time < current_time:
                elevator.stop_time = 0
                elevator.finish_order()                
                    
                
                    

            
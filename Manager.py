
import pygame as pg
import time

order_completed = -1

class Manager:
    def __init__(self):
        self.update_time = 0
       
        
    def elevator_selection(self,floor,building,screen):
        dst = floor.number 
        min = float('inf')
        for elevator in building.elevators:  
            dst_distance = abs(elevator.absolute_stop - dst)/2  
            arrival_time = elevator.operation_duration + dst_distance - elevator.elapsed_time()
            if min > arrival_time: 
                min = arrival_time
                priority_elevator = elevator
        arrival_time = min        
        floor.request_in_process(arrival_time,screen)
        priority_elevator.send_order(dst)


    def call(self,building,event,screen):
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
                            floor.made_order = True
                            self.elevator_selection(floor,building,screen)


    def update_arrival_time(self,building,screen):
        current_time = time.time()
        for floor in building.floors:
            if floor.made_order and current_time - floor.start_clock >= 0.5:
                # time_past = int((current_time - floor.start_clock)*10)
                # print(time_past)
                floor.time_left -= 0.5
                # floor.time_left = int(floor.time_left*10)/10
                floor.draw_timer_display(screen,True)
                floor.start_clock = time.time()
                if  floor.time_left <= 0.0:
                    floor.made_order = False
                    floor.draw_timer_display(screen,False)
                    floor.drew_button(screen, floor.roof_position,order_completed)
                    
                    
    def find_direction(self,dest_y,elevator):
        return (dest_y - elevator.current_location)/abs(dest_y - elevator.current_location)                
                    
    def steps(self,dest_y,elevator):
        mov_direction = self.find_direction(dest_y,elevator)
        vector = mov_direction*2  
        elevator.current_location +=  vector
        if dest_y != elevator.current_location and mov_direction != self.find_direction(dest_y,elevator):
            elevator.current_location = dest_y  
                        
    def travels(self,screen,building):
        for elevator in building.elevators:         
            if elevator.dst != elevator.departure and elevator.in_travel:
                dest_y = building.floors[elevator.dst].roof_position     
                if dest_y != elevator.current_location:
                    self.steps(dest_y,elevator)
                    building.update_elevators(screen)
                    print(time.time()-elevator.start_clock,elevator.current_location)
                else:
                    elevator.stop_time = time.time()
                    elevator.in_travel = False
                    
                    
    
    def close_finish_orders(self,building):
        current_time = time.time()
        for elevator in building.elevators:
            dest_y = building.floors[elevator.dst].roof_position
            if dest_y == elevator.current_location and 2 <= current_time - elevator.stop_time < current_time:
                elevator.stop_time = 0
                elevator.finish_order()                
                    
                
                    

            
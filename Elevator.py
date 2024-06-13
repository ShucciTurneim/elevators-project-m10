from collections import deque
import pygame as pg
import time
from Data_base import *

class Elevator:
    def __init__(self, number):
     # variables of creating elevator
        self.number = number
        self.width_position = 0
        self.position = 0
        self.current_location = 0
        
     # variables of elevator travel
        self.que = deque()
        self.absolute_stop = 0
        self.departure = 0           # self.que.popleft
        self.operation_duration = 0  # sum of all times of objects in q
        self.dst = 0
        self.in_travel = False
        self.stand_by = False
        self.stop_time = 0
        self.start_clock = 0
    
                
                        #Updates location of elevator During the construction phase and the travel phase
    def Recolor_screen(self,screen):                    
        rect = pg.Rect(self.width_position, self.current_location ,width_elevator,height_elevator)
        screen.fill(screen_color,rect)                
                        
    def update_location(self, screen):
            self.position = self.width_position,self.current_location   # --> x,y  
            self.Recolor_screen(screen)
            screen.blit(elevator_IMAGE, (self.position))

        
     # operations of creating elevator
    def build_elevator(self, num_elevator, screen):
        screen_height = pg.display.get_surface().get_height()
        self.width_position = (num_elevator * width_elevator + floor_width + timer_width)
        self.height_position = (screen_height - height_elevator)
        self.current_location =  self.height_position                   # in the Y axis     
        self.update_location(screen)
        
        
    # operations of elevator travels:
    
    # Calculates arrival time to a given destination
    def arrival_time(self, dst):
        """ dst = floor_number """
        dst_distance = abs(self.absolute_stop - dst)/2  
        return  self.operation_duration + dst_distance - self.elapsed_time()
        
        
        #Order confirmation management:Includes: queue management, operation time measurement, Update expected duration of action.
    def send_order(self, dst):
        new_travel_duration = (abs(dst - self.absolute_stop)/2) + stand_by
        self.operation_duration += new_travel_duration                                   # Update expected duration of action
        if not self.que:                                                                 #
            self.start_clock = time.time()
        self.que.append(dst)                                                             # queue management
        self.absolute_stop = self.que[-1]
        self.dst = self.que[0]
        if self.stop_time == 0:                                                          # Update status
            self.in_travel = True
            
    # Calculation of time remaining until the end of all elevator activity
    def elapsed_time(self):
        if self.start_clock != 0:               # Makes sure the elevator is in operation
            current_time = time.time()
            return current_time - self.start_clock
        else:
            return 0        
       
                           #travel_functions
                           
    def find_direction(self,dest_y):
        return (dest_y - self.current_location)/abs(dest_y - self.current_location)                
                    
                    
          #Calculation of the new position: including movement direction and step size.          
    def steps(self,dest_y):
        mov_direction = self.find_direction(dest_y)
        step_size = 2
        vector = mov_direction*step_size
        self.current_location +=  vector               
        #In case the elevator missed the target         
        if dest_y != self.current_location and mov_direction != self.find_direction(dest_y):
            self.current_location = dest_y  


    # Directs the progress of the journey, or ends it: including a change of status, Play a sound and reset the clock
    def travel(self,dest_y,screen):                                            
        if dest_y != self.current_location:
            self.steps(dest_y)
            self.Recolor_screen(screen)
            self.update_location(screen)
        else:                                       # ends : including a change of status, Play a sound and reset the clock
            self.stop_time = time.time()
            self.in_travel = False
            pg.mixer.music.load(ding)
            pg.mixer.music.play()
    
    
    def finish_order(self, dest_y, current_time):
        # Verify waiting time
        if dest_y == self.current_location and stand_by <= current_time - self.stop_time < current_time:
            self.stop_time = 0                                                  # reset the stand_by-clock
            ended_travel_duration = abs(self.departure - self.dst)/2 +stand_by  
            self.operation_duration -= ended_travel_duration                    # Reduces elapsed travel time
            self.departure = self.que.popleft()                                 # Queue management
            if self.que:
                self.dst = self.que[0]
                self.in_travel = True
                self.start_clock = time.time()
            else:    
                self.start_clock = 0                                             # reset the Operation time counter clock

    
            

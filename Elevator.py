from collections import deque
# import pygame as pg
from Floor import Floor
import time

stand_by = 2


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
        
    #for global use


     # operations of creating elevator
    def build_elevator(self, num_elevator, screen_height, A):
        self.width_position = (num_elevator * A.width_elevator + A.floor_width + A.timer_width)
        self.height_position = (screen_height - A.height_elevator)
        self.current_location =  self.height_position
        
    # operations of elevator travels
        
    def send_order(self, dst):
        new_travel_duration = (abs(dst - self.absolute_stop)/2) + stand_by
        self.operation_duration += new_travel_duration
        if not self.que:
            self.start_clock = time.time()
        self.que.append(dst)    
        self.absolute_stop = self.que[-1]
        self.dst = self.que[0]
        if self.stop_time == 0:
            self.in_travel = True
            
    
    def elapsed_time(self):
        if self.start_clock != 0:
            current_time = time.time()
            return current_time - self.start_clock
        else:
            return 0        
    
    
    def finish_order(self):
        ended_travel_duration = abs(self.departure - self.dst)/2 +2 #standby_time
        self.operation_duration -= ended_travel_duration
        self.departure = self.que.popleft()
        if self.que:
            self.dst = self.que[0]
            self.in_travel = True
            self.start_clock = time.time()
        else:    
            self.start_clock = 0

    
            

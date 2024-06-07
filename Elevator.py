from collections import deque
import pygame as pg
import pygame.mixer
from Floor import Floor
import time
width_elevator = 200
height_elevator = Floor.height()
stand_by = 2
screen_color =(255,255,255)


class Elevator:
    def __init__(self, number):
     # variables of creating elevator
        self.number = number
        self.width = width_elevator
        self.height = height_elevator
        self.width_position = 0
        self.position = 0
        self.current_location = 0
        self.path_img = "elv.png"
        img = pg.image.load(self.path_img)
        self.IMAGE = pg.transform.scale(img, (width_elevator, height_elevator))

    # variables of elevator travel
        self.que = deque()
        self.absolute_stop = 0
        self.departure = 0  # self.que.popleft
        self.operation_duration = 0  # sum of all times of objects in q
        self.dst = 0
        self.in_travel = False
        self.stand_by = False
        self.stop_time = 0
        self.start_clock = 0
        
    #for global use
    def width():
        return width_elevator

     # operations of creating elevator
    def build_elevator(self, num_elevator, screen_height, screen):
        self.width_position = (num_elevator * self.width + Floor.width() + Floor.timer_width())
        self.height_position = (screen_height - self.height)
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
    
    
    def finish_order(self):
        print("hell")
        ended_travel_duration = abs(self.departure - self.dst)/2 +2 #standby_time
        self.operation_duration -= ended_travel_duration
        self.departure = self.que.popleft()
        if self.que:
            self.dst = self.que[0]
            self.in_travel = True
            self.start_clock = time.time()
        else:    
            self.start_clock = 0
       # sound =  pg.mixer.Sound(floor.sound_voice)    
        # sound.play()
    
    def elapsed_time(self):
        if self.start_clock != 0:
            current_time = time.time()
            return current_time - self.start_clock
        else:
            return 0
            

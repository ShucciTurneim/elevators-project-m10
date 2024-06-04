from collections import deque
# from Architect import Building
import pygame as pg
from Floor import Floor
import time
width_elevator = 64
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
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/elv.png"
        img = pg.image.load(self.path_img)
        self.IMAGE = pg.transform.scale(img, (width_elevator, height_elevator))

    # variables of elevator travel
        self.que = deque()
        self.absolute_stop = 0
        self.departure = 0  # self.que.popleft
        self.next_stop = 0
        self.operation_duration = 0  # sum of all times of objects in q
        self.dst = 0
        self.travels = False
        
    #for global use
    def width():
        return width_elevator

     # operations of creating elevator
    def build_elevator(self, num_elevator, screen_height, screen):
        self.width_position = (num_elevator * self.width + Floor.width() + Floor.timer_width())
        self.height_position = (screen_height - self.height)
        self.current_location =  self.height_position
        
        
        
    

        # operations of elevator travel
    def send_order(self, floor, building, screen):
        new_travel_duration = (abs(floor - self.absolute_stop)/2) + stand_by
        self.operation_duration += new_travel_duration
        self.que.append(floor)    
        self.next_stop = self.que[0]
        self.absolute_stop = self.que[-1]
        self.dst = self.next_stop
        self.travels = True
        

    def finish_order(self,building):
        ended_travel_duration = abs(self.departure - self.next_stop)/2 +2 #standby_time
        self.operation_duration -= ended_travel_duration
        self.departure = self.que.popleft()
        floor = building.floors[self.dst]
        floor.made_order = False
        if self.que:
            self.dst = self.que[0]
        sound =  pg.mixer.Sound(floor.sound_voice)    
        sound.play()
               
        

        
    def elapsed_time(self,building):
        next_stop = self.next_stop
        return (abs(next_stop - self.departure)/2)  - building.floors[next_stop].floor_timer
    
    # def save_img(small_x, big_x, small_y, big_y, screen):
    #     reconstruction = {}
    #     for y in range(small_y,big_y+1):
    #         for x in range (small_x,big_x+1):
    #             reconstruction[(x,y)] = screen.get_at(x,y)
    #     return reconstruction
    
            

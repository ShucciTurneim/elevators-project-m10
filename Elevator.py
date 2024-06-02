from collections import deque
import pygame as pg
from Floor import Floor
width_elevator = 64
height_elevator = Floor.height()
stand_by = 2


class Elevator:
    def __init__(self, number):
     # variables of creating elevator
        self.number = int
        self.width = width_elevator
        self.height = height_elevator
        self.left_side_position = 0  # (left wall + floor_width+timer_width)
        # self.right_side_position = self.left_side_position + self.width
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/elv.png"

    # variables of elevator travel
        self.que = deque()
        self.absolute_stop = 0
        self.departure = 0  # self.que.popleft
        self.next_stop = 0
        self.operation_duration = 0  # sum of all times of objects in q
        
    #for global use
    def width():
        return width_elevator

     # operations of creating elevator
    def build_elevator(self, num_elevator, screen_height, screen):
        self.position = (num_elevator * self.width + Floor.width() + Floor.timer_width())
        # self.right_side_position = self.left_side_position + self.width
        initial_location = (screen_height)
        # initial_location_ceiling = initial_location_floor + self.hight
        # picture = self.path_img
        img = pg.image.load(self.path_img)
        IMAGE = pg.transform.scale(img, (width_elevator, height_elevator))
        screen.blit(IMAGE, (self.position, initial_location - self.height))
        pg.display.flip()

        # operations of elevator travel
    def send_order(self, floor, building, screen):
        new_travel_duration = (abs(floor - self.absolute_stop)/2) + stand_by
        self.operation_duration += new_travel_duration
        print(self.operation_duration)
        self.que.append(floor)    
        self.next_stop = self.que[0]
        self.absolute_stop = self.que[-1]
        building.floors[floor].show_arrival_time(screen,self.operation_duration - stand_by)
        print(self.operation_duration)

    def finish_order(self):
        ended_travel_duration = abs(self.departure - self.next_stop)/2 +2 #standby_time
        self.operation_duration -= ended_travel_duration
        self.departure = self.que.popleft()
        print(self.operation_duration)
        print(self.departure)
        

    def elapsed_time(self,building):
        next_stop = self.next_stop
        return (abs(next_stop - self.departure)/2)  - building.floors[next_stop].floor_timer


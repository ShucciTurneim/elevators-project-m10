from collections import deque
import pygame as pg
# from Floor import Floor
# import floors


class Elevator:
    def __init__(self, number):
     # variables of creating elevator
        self.number = int
        self.width = 64
        self.hight = 64
        self.left_side_position = 0  # (left wall + floor_width+timer_width)
        self.right_side_position = self.left_side_position + self.width
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/elv.png"

    # variables of elevator travel
        self.que = deque
        self.absolute_stop = self.que[-1]
        self.departure = 0  # self.que.popleft
        self.next_stop = self.que[0]
        self.operation_duration = 0  # sum of all times of objects in q

     # operations of creating elevator
    def build_elevator(self, num_elevator, hight, screen):
        self.left_side_position = num_elevator * self.width + 64 + 64
        # self.right_side_position = self.left_side_position + self.width
        initial_location_floor = hight
        # initial_location_ceiling = initial_location_floor + self.hight
        # picture = self.path_img
        image = "/home/mefathim/Documents/elevators-project-m10/elv.png"
        img = pg.image.load(image)
        screen.blit(img, (self.left_side_position, initial_location_floor-64))
        pg.display.flip()

        # operations of elevator travel
    def send_order(self, floor):
        # (abs(floor_number- self.absolute_stop)/2)+2
        self.operation_duration += (floor.distance/2)+2
        self.que.append(floor)
        self.absolute_stop = self.que[-1]

    def finish_order(self):
        self.operation_duration -= abs(self.departure - self.next_stop)/2
        self.departure = self.que.extendleft
        self.next_stop = self.que[0]

    def elapsed_time(self,):
        return (abs(self.next_stop - self.departure)/2)-64      #-floor.timer

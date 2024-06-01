from Elevator import Elevator
import pygame as pg
from Floor import Floor


def elevators_builder(elevators_num, screen, screen_height):
    for num_elevator in range(elevators_num):
        elevator = f"elevator_{num_elevator}"
        elevator = Elevator(num_elevator)
        elevator.build_elevator(num_elevator, screen_height, screen)

def floors_builder(num_floors,screen, screen_height):
    for num_floor in range(num_floors):
        floor = f"floor_{num_floor}"
        floor = Floor(num_floor)
        floor.build_floor(num_floor,screen,screen_height)

def new_building_architect(floors_num, elevators_num, screen):
    screen_height = pg.display.get_surface().get_height()
    elevators_builder(elevators_num, screen, screen_height)
    floors_builder(floors_num,screen, screen_height)

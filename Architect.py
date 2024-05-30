from Elevator import Elevator
import pygame as pg
from Floor import Floor


def elevators_builder(elevators_num, screen, screen_height):
    for num_elevator in range(elevators_num):
        new_elevator = f"elevator_{num_elevator}"
        new_elevator = Elevator(num_elevator)
        new_elevator.build_elevator(num_elevator, screen_height, screen)

def floors_builder(num_floors,screen, screen_height):
    for num_floor in range(num_floors):
        floor = f"floor_{num_floor}"
        floor = Floor(num_floor)
        floor.build_floor(num_floor,screen,screen_height)


def new_building_architect(floors_num, elevators_num, screen):
    screen_height = pg.display.get_surface().get_height()
    elevators_builder(elevators_num, screen, screen_height)
    floors_builder(floors_num,screen, screen_height)
    # pg.init()
    # size = (width,hight)
    # screen = pg.display.set_mode(size)
    # pg.display.set_caption("game")
    # screen.fill(white)
    # pg.display.flip()
    # image ="/home/mefathim/Documents/elevators-project-m10/elv.png"
    # img = pg.image.load(image)
    # screen.blit(img,(0,hight-64))
    # pg.display.flip()

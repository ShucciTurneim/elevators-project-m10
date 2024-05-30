from Elevator import Elevator
import pygame as pg
# import Floor


def elevators_builder(elevators_num, screen):
    _, hight = pg.display.get_surface().get_size()
    for num_elevator in range(0, elevators_num ):
        new_elevator = f"elevator_{num_elevator}"
        new_elevator = Elevator(num_elevator)
        new_elevator.build_elevator(num_elevator, hight, screen)

# def floors_builder(floors_num):
#    width,_ = pg.display.get_surface().get_size()
#     for num_elevator in range(1,floors_num+1):
#         floor = f"floor_{num_elevator}"
#         floor = Floor
#         floor.build_floor(floors_num,screen,width)


def new_building_architect(floors_num, elevators_num, screen):
    elevators_builder(elevators_num, screen)
    # floors_builder(floors_num)
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

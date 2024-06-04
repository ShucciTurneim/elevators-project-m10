from Elevator import Elevator
import pygame as pg
from Floor import Floor
screen_color =(255,255,255)
class Building:
    # floor_0_position = 0
    def __init__(self) -> None:
        self.elevators = []
        self.floors =[]
        
    def update_elevators(self, screen):
        screen_height = pg.display.get_surface().get_height()   
        for elevator in self.elevators:
            elevator.position = elevator.width_position,elevator.current_location
            rect = pg.Rect(elevator.width_position, 0, elevator.width, screen_height)
            screen.fill(screen_color,rect)
            screen.blit(elevator.IMAGE, (elevator.position))
            pg.display.flip()

    def elevators_builder(self,elevators_num, screen, screen_height):
        for num_elevator in range(elevators_num):
            elevator = Elevator(num_elevator)
            elevator.build_elevator(num_elevator, screen_height, screen)
            self.elevators.append(elevator)
            # elevator.next_stop = self.floors[0]
        # Building.floor_0_position = self.elevators[0].roof_position
        self.update_elevators(screen)    

    def floors_builder(self,num_floors,screen, screen_height):
        for num_floor in range(num_floors):
            floor = Floor(num_floor)
            floor.build_floor(num_floor,screen,screen_height)
            self.floors.append(floor)


        


    def new_building_architect(self,floors_num, elevators_num, screen):
        screen_height = pg.display.get_surface().get_height()
        self.floors_builder(floors_num,screen, screen_height)
        self.elevators_builder(elevators_num, screen, screen_height)
        

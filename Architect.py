from Elevator import Elevator
import pygame as pg
from Floor import Floor
class Architect:
    def __init__(self) -> None:
        
        
        #colors
        self.black_space_color = (0, 0, 0)
        self.numbers_default_color = (225, 0, 0)
        self.numbers_on_hold_color = (255,215,0)
        self.button_default_color = (128, 128, 128)
        self.button_on_hold_color = (0, 128, 0 ,128)
        self.screen_color = (255,255,255)
        #floors dimensions
        self.floor_width_img = 100
        self.floor_width = self.floor_width_img
        self.black_space_thickness  = 7
        self.floor_height_img = ((self.floor_width//3)*2)-self.black_space_thickness
        self.floor_height = self.floor_height_img + self.black_space_thickness  
        self.timer_width = self.floor_height
        self.floor_right_side = self.timer_width + self.floor_width
        self.floor_width_position = self.timer_width
        #elevators dimensions
        self.height_elevator = self.floor_height
        self.width_elevator = 60
        #media
        self.ding = "ding.mp3"
        self.floor_path_img = "wall.png"
        self.floor_img = pg.image.load(self.floor_path_img)
        self.FLOOR_IMAGE = pg.transform.scale(self.floor_img, (self.floor_width_img, self.floor_height_img))
        self.elevator_path_img = "elv.png"
        self.elevator_img = pg.image.load(self.elevator_path_img)
        self.elevator_IMAGE = pg.transform.scale(self.elevator_img, (self.width_elevator, self.height_elevator))


        #Updates location of elevators During the construction phase and the travel phase
    def update_elevators(self, screen, manager):
        for elevator in manager.get_elevators():    # x,            y
            elevator.position = elevator.width_position,elevator.current_location      
            rect = pg.Rect(elevator.width_position, elevator.current_location , self.width_elevator, self.height_elevator)
            screen.fill(self.screen_color,rect)
            screen.blit(self.elevator_IMAGE, (elevator.position))

    def elevators_builder(self,elevators_num, screen, screen_height, manager):
        for num_elevator in range(elevators_num):
            elevator = Elevator(num_elevator)
            elevator.build_elevator(num_elevator, screen_height, self)
            manager.set_elevators(elevator)
        self.update_elevators(screen, manager)    

    def floors_builder(self,num_floors,screen, screen_height, manager):
        for num_floor in range(num_floors):
            floor = Floor(num_floor)
            floor.build_floor(num_floor,screen,screen_height, self)
            manager.set_floors(floor)

    def new_building_architect(self,floors_num, elevators_num, screen, manager):
        screen_height = pg.display.get_surface().get_height()
        self.floors_builder(floors_num,screen, screen_height, manager)
        self.elevators_builder(elevators_num, screen, screen_height, manager)
     
             
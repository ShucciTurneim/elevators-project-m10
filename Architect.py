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
        
        #initial creation of the background screen and dimensions 
    def screen_design(self,elevators_numbers,floors_number):
        width = (elevators_numbers) * self.width_elevator + self.floor_width + self.timer_width
        height = floors_number * self.floor_height - self.black_space_thickness
        pg.init()
        size = (width,height)
        screen = pg.display.set_mode(size)
        pg.display.set_caption("building_game")
        screen.fill(self.screen_color)
        return screen






             
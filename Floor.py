import pygame as pg
black = (0,0,0)
black_line = 7
width_img = 64
height_img = 57
class Floor:
    def __init__(self,number):
        #variables of creating floor
        self.number = int
        self.width_floor = width_img 
        self.height_floor = height_img + black_line
        # self.floors_ceiling = self.floors +self.width  
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/wall.png"
        self.timer_width = 64
        self.width_position = self.timer_width
        self.right_side = self.timer_width + self.width_position
     
    def build_floor(self, num_floor, screen, screen_height):
        roof_position = screen_height - (num_floor+1) * self.height_floor   
        img = pg.image.load(self.path_img)
        draw_left_position = [self.width_position,roof_position+black_line/2]
        draw_right_position = [self.right_side,roof_position+black_line/2]
        IMAGE = pg.transform.scale(img,(width_img,height_img))
        screen.blit(IMAGE,(self.width_position,roof_position + black_line))
        pg.draw.line(screen, black, draw_left_position , draw_right_position, 7)
        pg.display.flip()

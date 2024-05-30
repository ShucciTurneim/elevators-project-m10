import pygame as pg
class Floor:
    def __init__(self:number):
        #variables of creating floor
        self.number = int
        self.width_floor = 64   
        self.heigh_floor = 64
        self.floors_floor = 0
        self.floors_ceiling = self.floors +self.width  
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/breck wall (1).jpg.png"
        
        def build_floor(self,num_floor,screen):
            self.floors_floor = hight_screen - num_floor * self.heigh_floor 
            # self.floors_ceiling = self.floors_floor + self.heigh_floor
            self.left_side = 0 + timer.width
            # self.right_side = self.left_side + self.width_floor
            picture = self.path_img    
            img = pg.image.load(picture)
            screen.blit(img,(0,height-64))
            pg.display.flip()

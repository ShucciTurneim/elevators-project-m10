import pygame as pg
pg.init()
# for color or size changes, please change here
black_space_color = (0, 0, 0)
numbers_default_color = (225, 0, 0)
numbers_on_hold_color = (255,215,0)
button_default_color = (128, 128, 128)
button_on_hold_color = (0, 128, 0 ,128)
height_img = 57
width_img = 64
black_space_thickness  = 7
height = height_img + black_space_thickness
width = width_img
timer_width = 64
builder = order_completed = 1


class Floor:
    def __init__(self, number):
        # variables of creating floor
        self.number = number
        self.width = width
        self.height = height
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/wall.png"
        self.timer_width = timer_width
        self.roof_position = None
        self.width_position = self.timer_width
        self.right_side = self.timer_width + self.width_position
        self.button = None
        self.button_radius = None
        
    # for global use
    def black_space_thickness():
        return black_space_thickness    
    def height():
        return height
    def timer_width():
        return timer_width
    def width():
        return width
    
# operations of creating floor

    def design(self,num_floor,screen_height):
        self.roof_position = screen_height - (num_floor+1) * self.height
        width_button_position = self.width_position + width_img/2
        height_button_position = self.roof_position + black_space_thickness + height_img/2
        self.button = width_button_position,height_button_position
    
    def drew_floor_number(self, screen,roof_position, called_by):
        font = pg.font.Font(None, int(height_img/2))
        if called_by in (builder,order_completed):
            color = numbers_default_color
        else:
            color =  numbers_on_hold_color   
        number = font.render(f'{self.number}', True, color)
        text_r = number.get_rect()
        text_r.center = (self.button)
        screen.blit(number, text_r)

    def drew_button(self, screen,roof_position, called_by):
        self.button_radius = height_img/4
        if called_by in (builder,order_completed):
            color = button_default_color
        else:
            color =  button_on_hold_color   
        button = pg.draw.circle(screen, color, self.button, self.button_radius)
        self.drew_floor_number(screen,roof_position,called_by)

    def drew_roof(self, roof_position, screen):
        line_left_position = [self.width_position, roof_position+black_space_thickness /2]
        line_right_position = [self.right_side, roof_position+black_space_thickness /2]
        pg.draw.line(screen, black_space_color, line_left_position, line_right_position, 7)

    def build_floor(self, num_floor, screen, screen_height):
        self.design(num_floor,screen_height)
        img = pg.image.load(self.path_img)
        IMAGE = pg.transform.scale(img, (width_img, height_img))
        screen.blit(IMAGE, (self.width_position, self.roof_position + black_space_thickness ))
        self.drew_button(screen,self.roof_position, builder)
        self.drew_roof(self.roof_position, screen)
        pg.display.flip()

import pygame as pg
import time
pg.init()
# for color or size changes, please change here
black_space_color = (0, 0, 0)
screen_color = (255,255,255)
numbers_default_color = (225, 0, 0)
numbers_on_hold_color = (255,215,0)
button_default_color = (128, 128, 128)
button_on_hold_color = (0, 128, 0 ,128)
height_img = 57
width_img = 100
black_space_thickness  = 7
height = height_img + black_space_thickness
width = width_img
timer_width = 64
builder = order_completed = -1
order = 0


class Floor:
    def __init__(self, number):
        # variables of creating floor
        self.number = number
        self.width = width
        self.height = height
        self.path_img = "wall.png"
        self.timer_width = timer_width
        self.roof_position = None
        self.width_position = self.timer_width
        self.right_side = self.timer_width + self.width
        self.button = ()
        self.button_radius = ()
        self.sound_voice = "/home/mefathim/elevators-project-m10/ding.mp3"
        
        # variables of call
        self.floor_timer = 0
        self.time_left = 0.0
        self.made_order = False
        self.clock_position = 0
        self.timer_Rect = 0
        self.time_on = False
        self.start_clock = 0
        
    def get_id(self):
        return self.number
        
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
        self.clock_position = (0 + width_img/4,self.roof_position + black_space_thickness + height_img/4)
        position_and_size = 0,self.roof_position + black_space_thickness, self.timer_width, height_img
        self.timer_Rect = pg.Rect(position_and_size)
         
    
    def drew_floor_number(self, screen, roof_position, color):
        font = pg.font.Font(None, int(height_img/2)) 
        number = font.render(f'{self.number}', True, color)
        text_r = number.get_rect()
        text_r.center = (self.button)
        screen.blit(number, text_r)

    def drew_button(self, screen, roof_position, called_by):
        self.button_radius = height_img/4
        if called_by in (builder,order_completed):
            color = button_default_color
            color_number = numbers_default_color
        else:
            color =  button_on_hold_color  
            color_number = numbers_on_hold_color  
        button = pg.draw.circle(screen, color, self.button, self.button_radius)
        self.drew_floor_number(screen,roof_position,color_number)

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
        
    # #operations of call
    
    def draw_timer_display(self,screen,turn_on):
        if turn_on:    
            pg.draw.rect(screen, black_space_color, self.timer_Rect)
            font = pg.font.Font(None, int(height_img/2)) 
            number = font.render(f'{self.time_left}', True, button_on_hold_color)
            screen.blit(number, self.clock_position)        
        else:
            pg.draw.rect(screen, screen_color, self.timer_Rect) 

    def request_in_process(self,arrival_time,screen):
        arrival_time = int(arrival_time*10)/10
        self.time_left = arrival_time
        print(self.time_left)
        self.drew_button(screen, self.roof_position,order)
        self.draw_timer_display(screen,True)
        self.start_clock = time.time()
        

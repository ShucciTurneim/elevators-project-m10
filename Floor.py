import pygame as pg
import time
pg.init()
builder = order_completed = -1
order = 0

class Floor:
    def __init__(self, number):
        # variables of creating floor
        self.number = number
        self.roof_position = None
        self.button = ()
        self.button_radius = ()
            
        # variables of call
        self.time_left = 0.0
        self.made_order = False
        self.clock_position = 0
        self.timer_Rect = 0
        self.start_clock = 0

    def design(self,num_floor,screen_height,A):
        self.roof_position = screen_height - (num_floor+1) * A.floor_height
        width_button_position = A.floor_width_position + A.floor_width_img/2
        height_button_position = self.roof_position + A.black_space_thickness +A.floor_height_img/2
        self.button = width_button_position,height_button_position
        self.clock_position = (0 + A.floor_width_img/4,self.roof_position + A.black_space_thickness + A.floor_height_img/4)
        position_and_size = 0,self.roof_position + A.black_space_thickness, A.timer_width, A.floor_height_img
        self.timer_Rect = pg.Rect(position_and_size)
         
    
    def drew_floor_number(self, screen, roof_position, color,A):
        font = pg.font.Font(None, int(A.floor_height_img/2)) 
        number = font.render(f'{self.number}', True, color)
        text_r = number.get_rect()
        text_r.center = (self.button)
        screen.blit(number, text_r)

    def drew_button(self, screen, roof_position, called_by,A):
        self.button_radius = A.floor_width_img/4
        if called_by in (builder,order_completed):
            color = A.button_default_color
            color_number = A.numbers_default_color
        else:
            color =  A.button_on_hold_color  
            color_number = A.numbers_on_hold_color  
        pg.draw.circle(screen, color, self.button, self.button_radius)
        self.drew_floor_number(screen,roof_position,color_number, A)

    def drew_roof(self, roof_position, screen, A):
        line_left_position = [A.floor_width_position, roof_position+A.black_space_thickness /2]
        line_right_position = [A.floor_right_side, roof_position+A.black_space_thickness /2]
        pg.draw.line(screen, A.black_space_color, line_left_position, line_right_position, 7)

    def build_floor(self, num_floor, screen, screen_height, A):
        self.design(num_floor,screen_height, A)
        screen.blit(A.FLOOR_IMAGE, (A.floor_width_position, self.roof_position + A.black_space_thickness ))
        self.drew_button(screen,self.roof_position, builder,A)
        self.drew_roof(self.roof_position, screen, A)
        pg.display.flip()
        
    # #operations of call
    
    def draw_timer_display(self,screen,turn_on, A):
        if turn_on:    
            pg.draw.rect(screen, A.black_space_color, self.timer_Rect)
            font = pg.font.Font(None, int(A.floor_height_img/2)) 
            print_format = int(self.time_left*10)/10
            number = font.render(f'{print_format}', True, A.button_on_hold_color)
            screen.blit(number, self.clock_position)        
        else:
            pg.draw.rect(screen, A.screen_color, self.timer_Rect) 

    def request_in_process(self,arrival_time,screen, A):
        self.time_left = arrival_time
        self.start_clock = time.time()
        self.drew_button(screen, self.roof_position,order,A)
        self.draw_timer_display(screen,True, A)
        
        

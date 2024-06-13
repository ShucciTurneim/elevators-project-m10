import pygame as pg

        
#colors
black_space_color = (0, 0, 0)
numbers_default_color = (225, 0, 0)
numbers_on_hold_color = (255,215,0)
button_default_color = (128, 128, 128)
button_on_hold_color = (0, 128, 0 ,128)
screen_color = (255,255,255)


#floors dimensions
floor_width_img = 100
floor_width = floor_width_img
black_space_thickness  = 7
floor_height_img = ((floor_width//3)*2)-black_space_thickness
floor_height = floor_height_img + black_space_thickness  
timer_width = floor_height
floor_right_side = timer_width + floor_width
floor_width_position = timer_width


#elevators dimensions
height_elevator = floor_height
width_elevator = 60
#elevators activity
stand_by = 2

#media
ding = "ding.mp3"
floor_path_img = "wall.png"
floor_img = pg.image.load(floor_path_img)
FLOOR_IMAGE = pg.transform.scale(floor_img, (floor_width_img, floor_height_img))
elevator_path_img = "elv.png"
elevator_img = pg.image.load(elevator_path_img)
elevator_IMAGE = pg.transform.scale(elevator_img, (width_elevator, height_elevator))


#floor painting variables
builder = order_completed = -1
order = 0







             
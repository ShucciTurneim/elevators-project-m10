import pygame as pg
pg.init()
black = (0, 0, 0)
red = (225, 0, 0)
gray = (128, 128, 128)
black_line = 7
width_img = 64
height_img = 57


class Floor:
    def __init__(self, number):
        # variables of creating floor
        self.number = int
        self.width_floor = width_img
        self.height_floor = height_img + black_line
        self.path_img = "/home/mefathim/Documents/elevators-project-m10/wall.png"
        self.timer_width = 64
        self.width_position = self.timer_width
        self.right_side = self.timer_width + self.width_position

    def drew_floor_number(self, IMAGE):
        font = pg.font.Font(None, int(height_img/2))
        text_o = font.render(f'{self.number}', True, red)
        text_r = text_o.get_rect()
        text_r.center = (width_img/2, height_img/2)
        IMAGE.blit(text_o, text_r)

    def drew_button(self, IMAGE):
        radius = height_img/4
        button = pg.draw.circle(
            IMAGE, gray, (width_img/2, height_img/2), radius)

    def drew_roof(self, roof_position, screen):
        line_left_position = [self.width_position, roof_position+black_line/2]
        line_right_position = [self.right_side, roof_position+black_line/2]
        pg.draw.line(screen, black, line_left_position, line_right_position, 7)

    def build_floor(self, num_floor, screen, screen_height):
        self.number = num_floor
        roof_position = screen_height - (num_floor+1) * self.height_floor
        img = pg.image.load(self.path_img)
        IMAGE = pg.transform.scale(img, (width_img, height_img))
        self.drew_button(IMAGE)
        self.drew_floor_number(IMAGE)
        self.drew_roof(roof_position, screen)
        screen.blit(IMAGE, (self.width_position, roof_position + black_line))
        pg.display.flip()

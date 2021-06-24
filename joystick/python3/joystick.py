import pygame

class Joystick:
    def __init__(self, fid):
        pygame.init()
        pygame.joystick.init()
        self.js = pygame.joystick.Joystick(fid)
        self.js.init()

    def get_sticks(self):
        pygame.event.get()
        return -self.js.get_axis(0), -self.js.get_axis(1), -self.js.get_axis(2), -self.js.get_axis(3),self.js.get_button(6)
        # 0- steer/LS, 1- UD/LS(not used), 2- LR/RS(not used), 3- throttle(U/D)/RS, 6- brake button trigger

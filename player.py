from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#class of player
class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__()
        self.jump_height = 0
        self.y = 0.1
        self.mouse_sensitivity = Vec2(20,20)
        self.speed = 2.5
        self.cursor.scale = 0
        self.step_sound = Audio("sounds\step.mp3", loop = True, autoplay = False, pitch = 0.65, volume = 0.5)
        self.dx = 0.005 # for blowing away
        self.dy = 0.01  # for shaking camera

    #blows away!   
    def update(self):
        super().update()
        self.x -= self.dx 

    def input(self, key):
        if held_keys["w"] or held_keys["s"] or held_keys["a"] or held_keys["d"]:
            self.camera_pivot.y = self.camera_pivot.y + self.dy     #shaking of the camera
            if (self.camera_pivot.y >= 2.05):
                self.dy = -self.dy
            if (self.camera_pivot.y <= 1.95):
                self.dy = -self.dy
            if (self.step_sound.playing == False):                  #and step sounds
                self.step_sound.play()
        else:
            self.step_sound.stop()
        

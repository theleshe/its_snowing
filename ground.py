from ursina import *

#class of ground planes
class Ground(Entity):       
    def __init__(self, number_x, number_z, player ,**kwargs):
        super().__init__()
        self.model="plane"
        self.scale = Vec3(30,1,30)
        self.texture="textures\ground"
        self.collider="cube"
        self.position = Vec3(number_x * 30, 0, number_z * 30)   #thats for 3x3 plane
        self.player = player

    #procedure "generation"
    def update(self):
       if(self.player.position.x - self.position.x < -45):
           self.position = Vec3(self.position.x - 90, 0, self.position.z)
       if(self.player.position.x - self.position.x > 45):
           self.position = Vec3(self.position.x + 90, 0, self.position.z)
       if(self.player.position.z - self.position.z < -45):
           self.position = Vec3(self.position.x, 0, self.position.z  - 90)
       if(self.player.position.z - self.position.z > 45):
           self.position = Vec3(self.position.x, 0, self.position.z  + 90)
